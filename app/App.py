from flask import Flask
from flask import json
from flask import request
from Common import *
from selenium.common.exceptions import TimeoutException

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/automation/v1/booking', methods = ['POST'])
def run_booking():
    rdata = request.json
    aobj = MasterBooking()
    try:
        returndata = aobj.run(rdata['search_text'], rdata['cin'], rdata['cout'])
        return json.dumps(returndata)
    except TimeoutException:
        returndata = {"ERROR":"TIMEOUT"}
        return json.dumps(returndata)


@app.route('/automation/v1/goibibo', methods=['POST'])
def run_goibibo():
    rdata = request.json
    aobj = MasterGoibibo()
    try:
        returndata = aobj.run(rdata['search_text'], rdata['cin'], rdata['cout'])
        return json.dumps(returndata)
    except TimeoutException:
        returndata = {"ERROR":"TIMEOUT"}
        return json.dumps(returndata)

@app.route('/automation/v1/mmt', methods=['POST'])
def run_mmt():
    rdata = request.json
    aobj = MasterMMT()
    try:
        returndata = aobj.run(rdata['search_text'], rdata['cin'], rdata['cout'])
        return json.dumps(returndata)
    except TimeoutException:
        returndata = {"ERROR":"TIMEOUT"}
        return json.dumps(returndata)
    # if request.headers['Content-Type'] == 'text/plain':
    #     return "Text Message: " + request.data
    #
    # elif request.headers['Content-Type'] == 'application/json':
    #     return "JSON Message: " + json.dumps(request.json)
    #
    # else:
    #     return "415 Unsupported Media Type ;)"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
