from flask import Flask
from flask_restful import Api
from childrenevents.controller.routes import initialize_routes
from childrenevents.datebase.db import initialize_db


app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] =\
    'mysql+mysqlconnector://lidl:New_password_1@localhost:3306/lidl-test-db?auth_plugin=mysql_native_password'

api = Api(app)

initialize_db(app)
initialize_routes(api)

app.run()
