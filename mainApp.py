from flask import Flask,jsonify,request
import json
from pprint import pprint
import sys
from ExpoBackOff import paymentGateway

app = Flask(__name__)


@app.route('/payment' , methods=['POST'])
def USDriver():
    payment_data = request.get_json()
    payment_status = ExpoBackOff.paymentGateway()
    if status == "Success":
        return "Payment Completed"
    return "Payment Failed"
    

app.run(host='0.0.0.0',port=5000)