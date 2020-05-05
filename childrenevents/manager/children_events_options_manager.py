import doctest

from typing import List

from childrenevents.model.children_event_option import ChildrenEventOption
from childrenevents.model.event_venue import EventVenue


class ChildrenEventsOptionsManager:

    def __init__(self, children_event_options: List[ChildrenEventOption] = None):
        if children_event_options is None:
            children_event_options: List[ChildrenEventOption] = []
        self.children_event_options = children_event_options

    def add_events_options(self, children_event_options: List[ChildrenEventOption]):
        if children_event_options is not None:
            self.children_event_options += children_event_options

    def add_events_option(self, children_event_option: ChildrenEventOption):
        self.children_event_options += [children_event_option]

    def find_option_by_criterion(self,
                                 max_duration_in_minutes: int = None,
                                 max_price_in_uah: float = None,
                                 min_price_in_uah: float = None,
                                 quantity_of_children: int = None,
                                 venue: EventVenue = None
                                 ) -> List[ChildrenEventOption]:
        """
        >>> manager = ChildrenEventsOptionsManager([ChildrenEventOption(name="volleyball", price_in_uah=100),
        ... ChildrenEventOption(name="football", price_in_uah=150), ChildrenEventOption(name="disco", price_in_uah=10),
        ... ChildrenEventOption(name="it course", price_in_uah=20)])
        >>> manager.find_option_by_criterion(max_price_in_uah=100)
        [ChildrenEventOption(venue=EventVenue.MIXED, name=volleyball, contact_number=, price_in_uah=100, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=disco, contact_number=, price_in_uah=10, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=it course, contact_number=, price_in_uah=20, max_quantity_of_children=0, duration_in_minutes=0)]
        """
        founded_options: List[ChildrenEventOption] = []
        for event_option in self.children_event_options:
            if ((quantity_of_children is None) or (
                    event_option.max_quantity_of_children >= quantity_of_children)) and (
                    (max_price_in_uah is None) or (event_option.price_in_uah <= max_price_in_uah)) and (
                    (min_price_in_uah is None) or (event_option.price_in_uah >= min_price_in_uah)) and (
                    (max_duration_in_minutes is None) or (
                    event_option.duration_in_minutes <= max_duration_in_minutes)) and (
                    (venue is None) or (event_option.venue is venue) or (event_option.venue is EventVenue.MIXED)):
                founded_options += [event_option]
        return founded_options


def do_test():
    manager = ChildrenEventsOptionsManager([ChildrenEventOption(name="volleyball", price_in_uah=100),
                                            ChildrenEventOption(name="football", price_in_uah=150),
                                            ChildrenEventOption(name="disco", price_in_uah=10),
                                            ChildrenEventOption(name="it course", price_in_uah=20)])
    list_options = tuple(manager.find_option_by_criterion(max_price_in_uah=100))
    return str(list_options)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
