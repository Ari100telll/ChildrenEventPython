from typing import List

from childrenevents.ua.lviv.iot.model.children_event_option import ChildrenEventOption
from childrenevents.ua.lviv.iot.model.event_venue import EventVenue


class MasterClass(ChildrenEventOption):
    def __init__(self, name: str,
                 contact_number: str = "",
                 price_in_uah: float = 0,
                 max_quantity_of_children: int = 0,
                 duration_in_minutes: int = 0,
                 venue: EventVenue = EventVenue.MIXED,
                 special_skills: List[str] = None,
                 equipment: List[str] = None
                 ):
        super().__init__(name, contact_number, price_in_uah, max_quantity_of_children, duration_in_minutes, venue)
        if special_skills is None:
            special_skills: List[str] = []
        if equipment is None:
            equipment: List[str] = []
        self.special_skills = special_skills
        self.equipment = equipment

    def __str__(self):
        return 'MasterClass(' + ', '.join((f"{name}={value}" for name, value in self.__dict__.items())) + ')'


if __name__ == '__main__':
    print(MasterClass("First"))
