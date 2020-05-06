import copy
import json

from flask import Response, request
from childrenevents.model.sport_event import SportEvent
from flask_restful import Resource
from childrenevents.app import ma, db


class SportEventSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
            'id', 'name', 'contact_number', 'price_in_uah', 'max_quantity_of_children', 'duration_in_minutes', 'venue',
            'location', 'sport_equipment')


sport_event_schema = SportEventSchema()
sport_events_schema = SportEventSchema(many=True)


class SportEventsApi(Resource):
    def get(self):
        all_sport_events = SportEvent.query.all()
        result = sport_events_schema.dump(all_sport_events)
        sport_events = json.dumps(result)
        return Response(sport_events, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        new_sport_event = SportEvent(**body)
        db.session.add(new_sport_event)
        db.session.commit()
        return sport_event_schema.jsonify(new_sport_event)


class SportEventApi(Resource):
    def put(self, id):
        body = request.get_json()
        sport_event: SportEvent = SportEvent.query.get(id)
        print(str(sport_event).center(100, ' '))
        if sport_event is None:
            return Response(status=404)
        old_sport_event = copy.deepcopy(sport_event)
        sport_event.copy_params(**body)
        db.session.commit()
        return sport_event_schema.jsonify(old_sport_event)

    def delete(self, id):
        sport_event = SportEvent.query.get(id)
        if sport_event is None:
            return Response(status=404)
        db.session.delete(sport_event)
        db.session.commit()
        return Response(status=200)

    def get(self, id):
        sport_event = SportEvent.query.get(id)
        if sport_event is None:
            return Response(status=404)
        return sport_event_schema.jsonify(sport_event)
