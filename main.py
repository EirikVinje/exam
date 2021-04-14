from sqlalchemy import Column, Integer, String, create_engine, update, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from flask import Flask, jsonify
from flask_restful import Resource, Api
import requests
import json
from database import *

app = Flask(__name__)
api = Api(app)

engine = create_engine('sqlite:///car_rental.sqlite')
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def get_cars():
    dict_list = []
    allcars = session.query(Cars).filter().all()
    # onecar = dict(session.query(Cars).get(12533))
    for car in allcars:
        dict_list.append(dict(id=car.id,
                              car_model=car.car_model,
                              prod_year=car.prod_year,
                              price_a_week=car.price_a_week))
    session.close()
    return jsonify(dict_list)


engine = create_engine('sqlite:///car_rental.sqlite')
Session = sessionmaker(bind=engine)
session_2 = Session()


@app.route('/customers')
def get_customers():
    dict_list = []
    allcustomers = session_2.query(Customer).filter().all()
    for customer in allcustomers:
        dict_list.append(dict(id=customer.id,
                              last_name=customer.Last_name,
                              first_name=customer.first_name,
                              phone_number=customer.phone_number))
    session_2.close()
    return jsonify(dict_list)



# api.add_resource(GetCars, '/')

# app.route('/Cars/Tenancy/Customer')

# app.route('/Cars')
# request.post/add/put/get

# app.route('/Cars/Tenancy')
# request.post/add/put/get

app.run(debug=True)
