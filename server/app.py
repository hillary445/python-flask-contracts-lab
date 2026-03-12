#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def home():
    return "<h1> Welcome to the contracts system</h1>"

@app.route('/contract/<int:id>')
def get_contract(id):
    item = next((x for x in contracts if x["id"] == id), None)
    if item:
        return item, 200
    else:
        return {"Error": "Not found"} , 404

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name.lower() in customers:
        return "", 204
    else:
        return {"Error": "Customer not found"}, 404
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
