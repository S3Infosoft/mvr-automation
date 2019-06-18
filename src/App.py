from flask import Flask
from flask import json
from flask import request

from Common import run

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/automation', methods = ['POST'])
def api_message():
    # {"ota_name": "0", "month_year": "June 2019", "cin": "22 24"}
    rdata = request.json
    run(rdata['ota_name'],rdata['month'],rdata['year'], rdata['cin'], rdata['cout'])
    return "JSON Message: " + json.dumps(request.json)
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
