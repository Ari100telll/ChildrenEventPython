from typing import List

from childrenevents.ua.lviv.iot.model.children_event_option import ChildrenEventOption
from childrenevents.ua.lviv.iot.model.event_venue import EventVenue


class SportEvent(ChildrenEventOption):
    def __init__(self, name: str,
                 contact_number: str = "",
                 price_in_uah: float = 0,
                 max_quantity_of_children: int = 0,
                 duration_in_minutes: int = 0,
                 venue: EventVenue = EventVenue.MIXED,
                 location: str = "",
                 sport_equipment: List[str] = None
                 ):
        super().__init__(name, contact_number, price_in_uah, max_quantity_of_children, duration_in_minutes, venue)
        if sport_equipment is None:
            sport_equipment: List[str] = []
        self.location = location
        self.sport_equipment = sport_equipment

    def __str__(self):
        return 'SportEvent(' + ', '.join((f"{name}={value}" for name, value in self.__dict__.items())) + ')'


if __name__ == '__main__':
    print(SportEvent("First"))
