from flask import Flask
from flask import json
from flask import request
from bookingdotcom import BookingDotComImpl
from goibibo import GoibiboImpl
from mmt import MMTImpl

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


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/automation/v1/booking', methods=['POST'])
def automation_booking():
    rdata = request.json
    target = BookingDotComImpl(rdata['search_text'], rdata['hotel_id'], rdata['checkin_date'],
                               rdata['checkout_date'], rdata['room_typeids'], rdata['room_priceids'])
    r = target.run()
    result = OtaRunResponse(r['ota'], r['run_start_time'], r['check_in'], r['check_out'],
                            r['Status'], r['run_end_time'], None)
    if r['Status'] == 'OK':
        result.set_rates(r['rates'], r['listed_position'])
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
    app.run(host='0.0.0.0')
