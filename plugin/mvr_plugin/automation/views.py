from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .tasks import *
import pymongo
import datetime
from bson.objectid import ObjectId
from .local1 import *
from .regular1 import *
from django.http import JsonResponse


class vars():

    grid_var = 0
    zel_var = 0
    process_list=[]
    #
    # def __init__(self):
    #     self.zel_var=0
    #     self.grid_var=0
    #     self.process_list=[]

    @staticmethod
    def inc_g_var():
        vars.grid_var += 1

    @staticmethod
    def dec_g_var():
        vars.grid_var -= 1

    @staticmethod
    def get_g_var():
        return vars.grid_var

    @staticmethod
    def inc_z_var():
        vars.zel_var += 1

    @staticmethod
    def dec_z_var():
        vars.zel_var -= 1

    @staticmethod
    def get_z_var():
        return vars.zel_var

    @staticmethod
    def append_to_list(item):
        vars.process_list.append(item)

    @staticmethod
    def delete_from_list(i):
        return vars.process_list.pop(i)


def inc_g_var():
    vars.grid_var += 1


def dec_g_var():
    vars.grid_var -= 1


def get_g_var():
    return vars.grid_var


def inc_z_var():
    vars.zel_var += 1


def dec_z_var():
    vars.zel_var -= 1


def get_z_var():
    return vars.zel_var


def append_to_list(item):
    vars.process_list.append(item)


def delete_from_list(i):
    return vars.process_list.pop(i)


def homepage(request):
    # delete_data()
    # tests=retrive_data()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mvr_result_set"]
    data = mydb.Completed_test_set
    # data.delete_many({})
    outputs = data.find()
    l=[]
    for i in outputs:
        print(i,'hi')
        ids=str(i['_id'])
        ota=i['ota']
        start_date=i['start_date']
        end_date=i['end_date']
        comments=i['comments']
        checkin=i['cindate']
        checkout=i['coutdate']
        status=i['status']
        d={'ids':ids,'ota':ota,'start_date':start_date,'comments':comments,'end_date':end_date,
           'checkin':checkin,'checkout':checkout,'status':status}
        l.append(d)
    print(outputs)
    l.reverse()
    print(l)
    param={'tests':l}
    return render(request,'automation/index.html',param)

def automate(request):
    cindate=request.GET.get('cindt')
    coutdate=request.GET.get('coutdt')
    agent=request.GET.get('agt')
    # cindate=request.POST.get('checkin',None)
    # coutdate=request.POST.get('checkout',None)
    # agent=request.POST.get('agt',None)
    current_time = datetime.datetime.now()
    print('a')
    start_date = current_time.strftime("%Y-%m-%d")
    id = data_entry(agent, "", start_date, "", "Started", "Succesfully started", "",cindate,coutdate)
    cur_sel_process=vars.get_g_var()
    cur_zel_process=vars.get_z_var()
    print(cur_zel_process,cur_sel_process)
    if cur_sel_process>=2:
        if cur_zel_process>=2:
            vars.append_to_list(id)
        else:
            plugin='zelenium'
    elif cur_sel_process<2:
        plugin='selenium grid'

    if cur_sel_process<2 or cur_zel_process<2:
        if agent == 'booking':
            # id = data_entry("Booking.com", "", start_date, "", "Started", "Succesfully started","")
            retrive_data()
            # return redirect("/automation/v1/booking/" + cindate + "/" + coutdate + "/" + id, code=307)
            automation_for_booking.delay(cindate,coutdate,id,plugin)
        elif agent == 'goibibo':
            # id = data_entry("Goibibo.com", "", start_date, "", "Started", "Succesfully started","")
            return redirect("/automation/v1/goibibo/" + cindate + "/" + coutdate + "/" + id, code=307)
        elif agent == 'mmt':
            # id = data_entry("Make my trip", "", start_date, "", "Started", "Succesfully started","")
            return redirect("/automation/v1/mmt/" + cindate + "/" + coutdate + "/" + id, code=307)

    tests = retrive_data()
    param = {'tests': tests}
    return render(request, 'automation/index.html', param)


def automate1(request):
    # cindate=request.GET.get('cindt')
    # coutdate=request.GET.get('coutdt')
    # agent=request.GET.get('agt')
    dt=request.POST.get('dt',None)
    print(dt)
    cindate,coutdate,agent=dt.split('@')
    print(cindate,coutdate,agent)
    # coutdate=request.POST.get('checkout',None)
    # agent=request.POST.get('agt',None)
    current_time = datetime.datetime.now()
    print('a')
    start_date = current_time.strftime("%Y-%m-%d")
    id = data_entry(agent, "", start_date, "", "Started", "Succesfully started", "",cindate,coutdate)
    cur_sel_process=vars.get_g_var()
    cur_zel_process=vars.get_z_var()
    print(cur_zel_process,cur_sel_process)
    if cur_sel_process>=1:
        if cur_zel_process>=2:
            vars.append_to_list(id)
        else:
            plugin='zelenium'
    elif cur_sel_process<1:
        plugin='selenium grid'

    if cur_sel_process<1 or cur_zel_process<2:
        if agent == 'booking':
            # id = data_entry("Booking.com", "", start_date, "", "Started", "Succesfully started","")
            retrive_data()
            # return redirect("/automation/v1/booking/" + cindate + "/" + coutdate + "/" + id, code=307)
            automation_for_booking(cindate,coutdate,id,plugin)
        elif agent == 'goibibo':
            # id = data_entry("Goibibo.com", "", start_date, "", "Started", "Succesfully started","")
            return redirect("/automation/v1/goibibo/" + cindate + "/" + coutdate + "/" + id, code=307)
        elif agent == 'mmt':
            # id = data_entry("Make my trip", "", start_date, "", "Started", "Succesfully started","")
            return redirect("/automation/v1/mmt/" + cindate + "/" + coutdate + "/" + id, code=307)
    data={'id':id}
    return JsonResponse(data)


def data_entry(ota,response,start_date,end_date,status,comment,plugin,cindate,coutdate):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["mvr_result_set"]
    mycol=mydb["Completed_test_set"]
    result={'start_date':start_date,
            'end_date':end_date,
            'ota':ota,
            'response':response,
            'status':status,
            'plugin':plugin,
            'comments':comment,
            'cindate':cindate,
            'coutdate':coutdate}
    x = mycol.insert_one(result)
    assign_id=x.inserted_id
    return str(assign_id)

def update_entry(id,end_date,response,status,comment,plugin,cindate,coutdate):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mvr_result_set"]
    mycol = mydb["Completed_test_set"]
    new_result={"$set":{'end_date':end_date,'response':response,'status':status,'comments':comment,'plugin':plugin,'cindate':cindate,'coutdate':coutdate}}
    mycol.update_one({'_id':ObjectId(id)},new_result)
    # result = mycol.find({'_id': ObjectId(id)})
    # result = eval(dumps(result))
    # print(result[0])

def retrive_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mvr_result_set"]
    data=mydb.Completed_test_set
    # data.delete_many({})
    outputs=data.find()
    for item in outputs:
        print(item)
    return outputs

def delete_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mvr_result_set"]
    data = mydb.Completed_test_set
    data.delete_many({})

    print('deleted all document successfully')

def booking_run(clint,checkin = "26/05/2020",checkout = "15/06/2020"):
    agent = Booking()
    search_text = "Ratnagiri"
    hotel_name = "Mango Valley Resort Ganpatipule"
    hotel_id = "4216443"
    room_typeids = ["room_type_id_421644306", "room_type_id_421644302",
                    "room_type_id_421644305", "room_type_id_421644303"]
    room_priceids = ["421644306_174652031_0_42_0",
                     "421644302_141698786_0_42_0", "421644302_174652031_0_42_0",
                     "421644305_174652031_0_42_0", "421644303_174652031_0_42_0"]

    # hotel_name="The Blue View - sea view villa's"
    # hotel_id="2808749"
    # room_typeids=[
    # #    'room_type_id_280874901']
                  # 'room_type_id_280874905']
    # room_priceids=[
       ## '280874901_229832000_0_41_0']
        # '280874905_229832000_0_41_0']
    result=main_run(agent, hotel_id, search_text, checkin, checkout,hotel_name,clint,room_typeids=room_typeids, room_priceids=room_priceids)
    print(result)
    return result

def automation_for_booking(cindate,coutdate,id,plugin):
    if plugin=='selenium grid':
        vars.inc_g_var()
        clint='http://192.168.56.1:4444/wd/hub'
    elif plugin=='zelenium':
        vars.inc_z_var()
        clint='http://192.168.99.100:4444/wd/hub'
    yr,month,date=cindate.split('-')
    checkin = date+"/"+month+"/"+yr
    yr, month, date = coutdate.split('-')
    checkout = date + "/" + month + "/" + yr
    current_time = datetime.datetime.now()
    end_date = current_time.strftime("%Y-%m-%d")
    try:
        result=booking_run(clint,checkin,checkout)
        update_entry(id, end_date,result, "Finished", "Succesfully completed",plugin,cindate,coutdate)
        # print(result)
        # return render_template('result.html',param=result)
    except Exception as e:
        print(e.__class__.__name__)
        update_entry(id, end_date, "No result", "Error", e.__class__.__name__,plugin,cindate,coutdate)
        # return f"Error occured of type {e.__class__.__name__}"

    if plugin == 'selenium grid':
        vars.dec_g_var()
    elif plugin == 'zelenium':
        vars.dec_z_var()

    no_of_pending_process=len(vars.process_list)
    for i in range(no_of_pending_process):
        # if no_of_pending_process>0:
            new_process=vars.process_list[i]
            print(new_process)
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mvr_result_set"]
            data = mydb.Completed_test_set
            output = data.find({'_id':ObjectId(new_process)})
            print(output)
            for m in output:
                l=m
            # k=0
            if(l['ota']=='booking'):
                prcs=vars.delete_from_list(i)
                automation_for_booking(l['cindate'],l['coutdate'],new_process,plugin)
                # k=1


def result(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mvr_result_set"]
    data = mydb.Completed_test_set
    id=request.GET.get('id')
    process=data.find({'_id':ObjectId(id)})
    # output = data.find({'_id': ObjectId(process)})
    for i in process:
        res=i['response']
        res1=i
    print(res)
    return render(request,'automation/result.html',{'param':res,'res1':res1})


def heartbeat(request):
    return render(request,'automation/heartbeat.html')

def selheart(request):
    clint = 'http://192.168.56.1:4444/wd/hub'
    try:
        caps = DesiredCapabilities.CHROME.copy()
        driver = webdriver.Remote(
            command_executor=clint,
            # desired_capabilities=DesiredCapabilities.CHROME)
            desired_capabilities=caps)

        driver.get('https://www.google.com/')
        driver.quit()
        return HttpResponse('working')
    except Exception as e:
        return  HttpResponse('Not woking due to <b>'+str(e)+'</b> error')


def zelheart(request):
    clint = 'http://192.168.99.100:4444/wd/hub'
    try:
        caps = DesiredCapabilities.CHROME.copy()
        driver = webdriver.Remote(
            command_executor=clint,
            # desired_capabilities=DesiredCapabilities.CHROME)
            desired_capabilities=caps)

        driver.get('https://www.google.com/')
        driver.quit()
        return HttpResponse('working')
    except Exception as e:
        return HttpResponse('Not woking due to <b>' + str(e) + '</b> error')
