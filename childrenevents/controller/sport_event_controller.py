import copy
import json

from flask import Response, request
from childrenevents.model.sport_event import SportEvent
from flask_restful import Resource
from childrenevents.datebase.db import ma, db


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


class SportEventsApi(Resource):
    def get(self):
        all_sport_events = SportEvent.query.all()
        result = sport_events_schema.dump(all_sport_events)
        sport_events = json.dumps(result)
        return Response(sport_events, mimetype="application/json", status=200)

    def post(self):
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


class SportEventApi(Resource):
    def put(self, id):
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

    def delete(self, id):
        sport_event = SportEvent.query.get(id)
        db.session.delete(sport_event)
        db.session.commit()
        return '', 200

    def get(self, id):
        sport_event = SportEvent.query.get(id)
        return sport_event_schema.jsonify(sport_event)
