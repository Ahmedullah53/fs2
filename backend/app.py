import time

import redis
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return 'Hello World! I have been seen {} times.\n'.format(1)

@app.route('/customer-location/', methods=['GET'])
def customer_location():
    response_body = {
        "latitude": 24,
        "longitude": 67
    }
    res = make_response(jsonify(response_body), 200)
    return res

@app.route('/customer-details/', methods=['GET'])
def customer_details():
    response_body = {
        "name": "Ahmedullah Siddiqui",
        "email": "ahmedullah.siddiqui@tenpearls.com",
        "contact": "0322-9465316",
    }
    res = make_response(jsonify(response_body), 200)
    return res

@app.route('/driver-details/', methods=['GET'])
def driver_details():
    response_body = {
        "name": "Ahmedullah Siddiqui",
        "email": "ahmedullah.siddiqui@tenpearls.com",
        "contact": "0322-8227433",
        "vehicle": {
            "plates": "ABQ-700",
            "color": "green",
            "make": "Suzuki",
            "model": "Mehran",
        }
    }
    res = make_response(jsonify(response_body), 200)
    return res

@app.route('/driver-location/', methods=['GET'])
def driver_location():
    response_body = {
        "latitude": 24,
        "longitude": 67
    }
    res = make_response(jsonify(response_body), 200)
    return res