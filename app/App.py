from flask import Flask
from flask import json
from flask import request,render_template,redirect
from bookingdotcom import BookingDotComImpl
from goibibo import GoibiboImpl
from mmt import MMTImpl
from local import *
from regular import main_run
from regular import MasterMMT
from bson.json_util import dumps
from bson.objectid import ObjectId

import pymongo
import datetime
app = Flask(__name__)




class OtaRunResponse(object):
    def __init__(self, ota, run_start_time, cin, cout, status, run_end_time, comments):
        self.ota = ota
        self.run_start_time = run_start_time
        self.checkin = cin
        self.checkout = cout
        self.status = status
        self.comments = comments
        self.rates = {}
        self.listed = None
        self.run_end_time = run_end_time

    def set_rates(self, rates, listed):
        self.rates = rates
        self.listed = listed

    def get_json(self):
        data = {
            'ota': self.ota,
            'timestamp': self.run_end_time,
            'checkin': self.checkin,
            'checkout': self.checkout,
            'status': self.status,
            'run_start_time': self.run_start_time,
            'run_end_time': self.run_end_time
        }
        if self.rates:
            data['rates'] = self.rates
        if self.listed:
            data['listed_position'] = self.listed
        if self.comments:
            data['comments'] = self.comments
        return data

#

def data_entry(ota,response,start_date,end_date,status,comment):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["mvr_results"]
    mycol=mydb["Completed_test"]
    result={'start_date':start_date,
            'end_date':end_date,
            'ota':ota,
            'response':response,
            'status':status,
            'comments':comment}
    x = mycol.insert_one(result)
    assign_id=x.inserted_id
    return str(assign_id)

def update_entry(id,end_date,response,status,comment):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mvr_results"]
    mycol = mydb["Completed_test"]
    new_result={"$set":{'end_date':end_date,'response':response,'status':status,'comments':comment}}
    mycol.update_one({'_id':ObjectId(id)},new_result)
    # result = mycol.find({'_id': ObjectId(id)})
    # result = eval(dumps(result))
    # print(result[0])


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/automation/process_data",methods=['POST'])
def process_data():
    cindate=request.form['cindt']
    coutdate=request.form['coutdt']
    agent=request.form['agt']
    current_time = datetime.datetime.now()
    start_date = current_time.strftime("%Y-%m-%d")
    if agent=='booking':
        id=data_entry("Booking.com","",start_date,"","Started","Succesfully started")
        return redirect("/automation/v1/booking/"+cindate+"/"+coutdate+"/"+id,code=307)
    elif agent=='goibibo':
        id=data_entry("Goibibo.com","",start_date,"","Started","Succesfully started")
        return redirect("/automation/v1/goibibo/"+cindate+"/"+coutdate+"/"+id,code=307)
    elif agent=='mmt':
        id=data_entry("Make my trip", "", start_date, "", "Started", "Succesfully started")
        return redirect("/automation/v1/mmt/" + cindate + "/" + coutdate+"/"+id, code=307)

@app.route('/automation/v1/booking/<cindate>/<coutdate>/<id>', methods=['POST'])
def automation_for_booking(cindate,coutdate,id):
    agent = Booking()
    search_text = "Ratnagiri" # for booking
    hotel_name = "Mango Valley Resort Ganpatipule"
    yr,month,date=cindate.split('-')
    checkin = date+"/"+month+"/"+yr
    yr, month, date = coutdate.split('-')
    checkout = date + "/" + month + "/" + yr
    hotel_id = "4216443"
    current_time = datetime.datetime.now()
    end_date = current_time.strftime("%Y-%m-%d")
    room_typeids = ["room_type_id_421644306", "room_type_id_421644302",
                    "room_type_id_421644305", "room_type_id_421644303"]
    room_priceids = ["421644306_174652031_0_42_0",
                     "421644302_141698786_0_42_0", "421644302_174652031_0_42_0",
                     "421644305_174652031_0_42_0", "421644303_174652031_0_42_0"]
    # try:
    result=main_run(agent, hotel_id, search_text, checkin, checkout,room_typeids=room_typeids, room_priceids=room_priceids)
    update_entry(id, end_date,result, "Finished", "Succesfully completed")
    # print(result)
    return render_template('result.html',param=result)
    # except Exception as e:
    #     print(e.__class__.__name__)
    #     update_entry(id, end_date, "No result", "Error", e.__class__.__name__)
    #     return f"Error occured of type {e.__class__.__name__}"

@app.route('/automation/v1/goibibo/<cindate>/<coutdate>/<id>', methods=['POST'])
def automation_for_goibibo(cindate,coutdate,id):
    agent = Goibibo()
    search_text = "Ganpatipule"
    hotel_name = "Mango Valley Resort Ganpatipule"
    yr, month, date = cindate.split('-')
    checkin = date + "/" + month + "/" + yr
    yr, month, date = coutdate.split('-')
    checkout = date + "/" + month + "/" + yr
    room_ids = ["roomrtc_45000750981", "roomrtc_45000574663", "roomrtc_45000717373",
                           "roomrtc_45000574667"]
    current_time = datetime.datetime.now()
    end_date = current_time.strftime("%Y-%m-%d")
# try:
    result=main_run(agent, hotel_name, search_text, checkin, checkout, room_ids=room_ids)
    update_entry(id,end_date,result, "Finished", "Succesfully completed")
    return render_template('result.html', param=result)
    # except Exception as e:
    #     print(e.__class__.__name__)
    #     update_entry(id, end_date,"No result", "Error", e.__class__.__name__)
    #     return f"Error occured of type {e.__class__.__name__}"




@app.route('/automation/v1/mmt/<cindate>/<coutdate>/<id>', methods=['POST'])
def automation_for_mmt(cindate,coutdate,id):
    agent = MasterMMT()
    search_text = "Ganpatipule"
    hotel_name = "Mango Valley Resort Ganpatipule"
    yr, month, date = cindate.split('-')
    checkin = date + "/" + month + "/" + yr[:2]
    yr, month, date = coutdate.split('-')
    checkout = date + "/" + month + "/" + yr[:2]
    current_time = datetime.datetime.now()
    end_date = current_time.strftime("%Y-%m-%d")
    print(checkin)
    print(type(checkin))
    # checkin="13/03/20"
    # checkout="14/03/20"
    print(type(checkin))
    hotel_id = "201811281301162654"
    room_id = ["990001097019", "990001200931", "990001097020", "990001200939", "990001097021", "990001200965",
               "990001302537"]
    hotel_id = "201403202029134840"
    hotel_name = "Nakshatra Beach Resort by O'NEST"
    room_id = ["990000116124", "990000088134", "990000633744", "990000633727", "990001303500", "990000088158",
               "990000633761", "990001303499", "990000088270", "990000633777", "990001303498", "990000088272",
               "990000633793"]
    hotel_name = "Blue Ocean Resort & Spa"
    hotel_id = "200908241107085994"
    room_id = ["990000758441", "990000758470", "990000009534", "990000758436", "990000308366", "990000009536",
               "990000758437"]

    result = agent.run(search_text, hotel_id, hotel_name, checkin, checkout, room_id)
    print(result)
    update_entry(id, end_date,result, "Finished", "Succesfully completed")
    return render_template('result.html', param=result)
    # except Exception as e:
    #     print(e.__class__.__name__)
    #     update_entry(id, end_date,"No result", "Error", e.__class__.__name__)
    #     return f"Error occured of type {e.__class__.__name__}"





@app.route('/automation/v1/booking/', methods=['POST'])
def automation_booking():
    rdata = request.json
    target = BookingDotComImpl(rdata['search_text'], rdata['hotel_id'], rdata['checkin_date'],
                               rdata['checkout_date'], rdata['room_typeids'], rdata['room_priceids'])
    r = target.run()
    result = OtaRunResponse(r['ota'], r['run_start_time'], r['check_in'], r['check_out'],
                            r['Status'], r['run_end_time'], None)
    if r['Status'] == 'OK':
        result.set_rates(r['rates'], r['listed_position'])
        print(result)
    return json.dumps(result.get_json())


@app.route('/automation/v1/mmt', methods = ['POST'])
def automation_mmt():
    rdata = request.json
    target = MMTImpl(rdata['search_text'], rdata['hotel_id'], rdata['hotel_name'],
                     rdata['checkin_date'], rdata['checkout_date'], rdata['room_id'])
    r = target.run()
    result = OtaRunResponse(r['ota'], r['run_start_time'], r['check_in'], r['check_out'],
                            r['Status'], r['run_end_time'], None)
    if r['Status'] == 'OK':
        result.set_rates(r['rates'], r['listed_position'])
    return json.dumps(result.get_json())


@app.route('/automation/v1/goibibo', methods = ['POST'])
def automation_goibibo():
    rdata = request.json
    target = GoibiboImpl(rdata['search_text'],rdata['hotel_name'], rdata['checkin_date'],
                         rdata['checkout_date'], rdata['room_ids'])
    r = target.run()
    result = OtaRunResponse(r['ota'], r['run_start_time'], r['check_in'], r['check_out'],
                            r['Status'], r['run_end_time'], None)
    if r['Status'] == 'OK':
        result.set_rates(r['rates'], r['listed_position'])
    return json.dumps(result.get_json())


@app.route('/automation/v1/yatra', methods = ['POST'])
def automation_yatra():
    rdata = request.json
    return json.dumps(rdata)


@app.route('/automation/v1/travelguru', methods = ['POST'])
def automation_tg():
    rdata = request.json
    return json.dumps(rdata)


@app.route('/automation/v1/airbnb', methods = ['POST'])
def automation_airbnb():
    rdata = request.json
    return json.dumps(rdata)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
