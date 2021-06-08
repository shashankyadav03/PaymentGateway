from flask import Flask,jsonify,request
import json
from pprint import pprint
import sys
from ExpoBackOff import paymentGateway

app = Flask(__name__)


@app.route('/payment' , methods=['POST'])
def USDriver():
    payment_data = request.get_json()
    pprint(payment_data)
    payment_status = paymentGateway()
    if payment_status == "Success":
        print("Payment Completed")
        return "Payment Completed"
    return "Payment Failed"
    

app.run(host='0.0.0.0',port=5000)