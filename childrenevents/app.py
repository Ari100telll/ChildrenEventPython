from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] =\
    'mysql+mysqlconnector://lidl:New_password_1@localhost:3306/lidl-test-db?auth_plugin=mysql_native_password'

api = Api(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == '__main__':
    from childrenevents.controller.routes import initialize_routes
    initialize_routes(api)
    app.run(debug=True)
