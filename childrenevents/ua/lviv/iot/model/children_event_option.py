from childrenevents.ua.lviv.iot.model.event_venue import EventVenue


class ChildrenEventOption:

    def __init__(self, name: str,
                 contact_number: str = "",
                 price_in_uah: float = 0,
                 max_quantity_of_children: int = 0,
                 duration_in_minutes: int = 0,
                 venue: EventVenue = EventVenue.MIXED
                 ):
        self.venue = venue
        self.name = name
        self.contact_number = contact_number
        self.price_in_uah = price_in_uah
        self.max_quantity_of_children = max_quantity_of_children
        self.duration_in_minutes = duration_in_minutes

    def __str__(self):
        return 'ChildrenEventOption(' + ', '.join((f"{name}={value}" for name, value in self.__dict__.items())) + ')'

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    print(ChildrenEventOption("first"))
