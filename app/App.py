from flask import Flask
from flask import json
from flask import request
from bookingdotcom import BookingDotComImpl
from goibibo import GoibiboImpl
from mmt import MMTImpl

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/automation/v1/booking', methods=['POST'])
def automation_booking():
    rdata = request.json
    target = BookingDotComImpl(rdata['search_text'], rdata['hotel_id'], rdata['checkin_date'], rdata['checkout_date'], rdata['room_typeids'], rdata['room_priceids'])
    result = target.run()
    return json.dumps(result)


@app.route('/automation/v1/mmt', methods = ['POST'])
def automation_mmt():
    rdata = request.json
    target = MMTImpl(rdata['search_text'], rdata['checkin_date'], rdata['checkout_date'])
    result = target.run()
    return json.dumps(result)


@app.route('/automation/v1/goibibo', methods = ['POST'])
def automation_goibibo():
    rdata = request.json
    target = GoibiboImpl(rdata['search_text'],rdata['hotel_name'], rdata['checkin_date'], rdata['checkout_date'])
    result = target.run()
    return json.dumps(result)


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
