from childrenevents.ua.lviv.iot.model.children_event_option import ChildrenEventOption
from childrenevents.ua.lviv.iot.model.event_venue import EventVenue


class CostumeParty(ChildrenEventOption):
    def __init__(self, name: str,
                 contact_number: str = "",
                 price_in_uah: float = 0,
                 max_quantity_of_children: int = 0,
                 duration_in_minutes: int = 0,
                 venue: EventVenue = EventVenue.MIXED,
                 price_for_one_costume_in_uah: float = 0,
                 topic: str = ""
                 ):
        super().__init__(name, contact_number, price_in_uah, max_quantity_of_children, duration_in_minutes, venue)
        self.price_for_one_costume_in_uah = price_for_one_costume_in_uah
        self.topic = topic

    def __str__(self):
        return 'CostumeParty(' + ', '.join((f"{name}={value}" for name, value in self.__dict__.items())) + ')'


if __name__ == '__main__':
    print(CostumeParty("First"))
