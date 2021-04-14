from sqlalchemy import Column, Integer, String, create_engine, update, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import json
from database import *
from werkzeug.exceptions import *

app = Flask(__name__)
api = Api(app)

engine = create_engine('sqlite:///car_rental.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
session_2 = Session()
session_3 = Session()
session_4 = Session()
session_5 = Session()
customers_list = []
cars_list = []


class Index(Resource):
    def get(self):
        return 'hello'


class GetCars(Resource):
    def get(self):
        allcars = session.query(Cars).all()
        # onecar = dict(session.query(Cars).get(12533))
        for car in allcars:
            cars_list.append(dict(id=car.id,
                                  car_model=car.car_model,
                                  prod_year=car.prod_year,
                                  price_a_week=car.price_a_week,
                                  customer_id=car.customer_id))
        session.close()
        return cars_list


class GetCustomers(Resource):
    def get(self):
        allcustomers = session_2.query(Customer).all()
        for customer in allcustomers:
            customers_list.append(dict(id=customer.id,
                                  last_name=customer.Last_name,
                                  first_name=customer.first_name,
                                  phone_number=customer.phone_number))
        session_2.close()
        return customers_list


class GetOneCustomer(Resource):
    def get(self, id_customer):
        for dictionary in customers_list:
            if id_customer == dictionary['id']:
                return dictionary
        raise NotFound(f'Costumer with id {id_customer} not found')

    def add(self):
        pass


class GetOneCar(Resource):
    def get(self, id_car):
        for dictionary in cars_list:
            if id_car == dictionary['id']:
                return dictionary
        raise NotFound(f'Car with id {id_car} not found')




api.add_resource(Index, '/')
api.add_resource(GetCars, '/cars')
api.add_resource(GetCustomers, '/customers/')
api.add_resource(GetOneCustomer, '/customers/<int:id_customer>')
api.add_resource(GetOneCar, '/cars/<int:id_car>')


app.run(debug=True)
