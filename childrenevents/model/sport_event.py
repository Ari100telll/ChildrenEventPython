import json
from typing import List

from sqlalchemy.ext.hybrid import hybrid_property

from childrenevents.app import db
from childrenevents.model.children_event_option import ChildrenEventOption
from childrenevents.model.event_venue import EventVenue


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

    def __init__(self, name: str, contact_number: str = "", price_in_uah: float = 0, max_quantity_of_children: int = 0,
                 duration_in_minutes: int = 0, venue: EventVenue = EventVenue.MIXED, location: str = "",
                 sport_equipment: List[str] = None):
        super().__init__(name, contact_number, price_in_uah, max_quantity_of_children, duration_in_minutes, venue)
        if sport_equipment is None:
            sport_equipment = []
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

    def copy_params(self, name: None, contact_number: str = None, price_in_uah: float = None,
                    max_quantity_of_children: int = None, duration_in_minutes: int = None, venue: EventVenue = None,
                    location: str = None, sport_equipment: List[str] = None):
        if name is not None:
            self.name = name
        if contact_number is not None:
            self.contact_number = contact_number
        if price_in_uah is not None:
            self.price_in_uah = price_in_uah
        if max_quantity_of_children is not None:
            self.max_quantity_of_children = max_quantity_of_children
        if duration_in_minutes is not None:
            self.duration_in_minutes = duration_in_minutes
        if venue is not None:
            self.venue = venue
        if location is not None:
            self.location = location
        if sport_equipment is not None:
            self.sport_equipment = sport_equipment


db.create_all()
