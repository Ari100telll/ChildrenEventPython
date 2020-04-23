from typing import List

from childrenevents.ua.lviv.iot.model import ChildrenEventOption
from childrenevents.ua.lviv.iot.model.event_venue import EventVenue


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
                                 ):
        founded_options: List[ChildrenEventOption] = []
        for option in self.children_event_options:
            if ((option.price_in_uah is None) or (
                    (option.price_in_uah <= max_price_in_uah) and (option.price_in_uah >= min_price_in_uah))) and (
                    (option.max_quantity_of_children is None) or (
                    option.max_quantity_of_children >= quantity_of_children)) and (
                    (option.duration_in_minutes is None) or (
                    option.duration_in_minutes <= max_duration_in_minutes)) and (
                    (option.venue is None) or (option.venue is venue) or (option.venue is EventVenue.MIXED)):
                founded_options += [option]
