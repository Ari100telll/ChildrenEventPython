import json

from typing import List

from children_event_option import ChildrenEventOption
from event_venue import EventVenue

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.ext.hybrid import hybrid_property
import copy
import mysql.connector
import os

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://lidl:New_password_1@localhost:3306/lidl-test-db?auth_plugin=mysql_native_password'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SportEvent(ChildrenEventOption, db.Model):
    name = db.Column(db.String(120), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    contact_number = db.Column(db.String(80))
    price_in_uah = db.Column(db.Float)
    max_quantity_of_children = db.Column(db.Integer)
    duration_in_minutes = db.Column(db.Integer)
    location = db.Column(db.String(80))
    venue = db.Column(db.Enum(EventVenue))
    _sport_equipment = db.Column('sport_equipment', db.String(255), default='[]', server_default='[]')

    __metaclass__ = ChildrenEventOption

    def __init__(self, name: str,
                 contact_number: str = "",
                 price_in_uah: float = 0,
                 max_quantity_of_children: int = 0,
                 duration_in_minutes: int = 0,
                 venue: EventVenue = EventVenue.MIXED,
                 location: str = "",
                 sport_equipment: List[str] = []
                 ):
        super().__init__(name, contact_number, price_in_uah, max_quantity_of_children, duration_in_minutes, venue)
        self.location = location
        self.sport_equipment = sport_equipment

    @hybrid_property
    def sport_equipment(self):
        return json.loads(self._sport_equipment)

    @sport_equipment.setter
    def sport_equipment(self, sport_equipment):
        self._sport_equipment = json.dumps(sport_equipment)

    def __str__(self):
        return 'SportEvent(' + ', '.join((f"{name}={value}" for name, value in self.__dict__.items())) + ')'

    def __repr__(self):
        return str(self)


class SportEventSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
            'id', 'name', 'contact_number', 'price_in_uah', 'max_quantity_of_children', 'duration_in_minutes', 'venue',
            'location',
            'sport_equipment'
        )


sport_event_schema = SportEventSchema()
sport_events_schema = SportEventSchema(many=True)


@app.route("/sport-event", methods=["POST"])
def add_sport_events():
    name = request.json['name']
    contact_number = request.json['contact_number']
    price_in_uah = request.json['price_in_uah']
    max_quantity_of_children = request.json['max_quantity_of_children']
    duration_in_minutes = request.json['duration_in_minutes']
    venue = request.json['venue']
    location = request.json['location']
    sport_equipment = request.json['sport_equipment']

    new_sport_event = SportEvent(name, contact_number, price_in_uah, max_quantity_of_children, duration_in_minutes,
                                 venue, location, sport_equipment)

    db.session.add(new_sport_event)
    db.session.commit()
    return sport_event_schema.jsonify(new_sport_event)


@app.route("/sport-event", methods=["GET"])
def get_sport_events():
    all_sport_events = SportEvent.query.all()
    result = sport_events_schema.dump(all_sport_events)
    return json.dumps(result)


@app.route("/sport-event/<id>", methods=["GET"])
def get_sport_event(id):
    sport_event = SportEvent.query.get(id)
    return sport_event_schema.jsonify(sport_event)


@app.route("/sport-event/<id>", methods=["PUT"])
def update_sport_event(id):
    sport_event = SportEvent.query.get(id)
    name = request.json['name']
    contact_number = request.json['contact_number']
    price_in_uah = request.json['price_in_uah']
    max_quantity_of_children = request.json['max_quantity_of_children']
    duration_in_minutes = request.json['duration_in_minutes']
    venue = request.json['venue']
    location = request.json['location']
    sport_equipment = request.json['sport_equipment']

    old_sport_event = copy.deepcopy(sport_event)

    sport_event.name = name
    sport_event.contact_number = contact_number
    sport_event.price_in_uah = price_in_uah
    sport_event.max_quantity_of_children = max_quantity_of_children
    sport_event.duration_in_minutes = duration_in_minutes
    sport_event.venue = venue
    sport_event.location = location
    sport_event.sport_equipment = sport_equipment

    db.session.commit()
    return sport_event_schema.jsonify(old_sport_event)


@app.route("/sport-event/<id>", methods=["DELETE"])
def delete_sport_event(id):
    sport_event = SportEvent.query.get(id)
    db.session.delete(sport_event)
    db.session.commit()

    return sport_event_schema.jsonify(sport_event)


if __name__ == '__main__':
    app.run(debug=True)
