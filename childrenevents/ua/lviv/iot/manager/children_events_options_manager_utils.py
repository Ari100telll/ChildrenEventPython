import doctest
from operator import attrgetter
from typing import List

from childrenevents.ua.lviv.iot.manager.children_events_options_manager import ChildrenEventsOptionsManager
from childrenevents.ua.lviv.iot.model import ChildrenEventOption
from childrenevents.ua.lviv.iot.model.sort_type import SortType


def sort_by_price(children_events_options_list: List[ChildrenEventOption], sort_type: SortType = SortType.ASCENDING):
    """
    >>> new_options_list = [ChildrenEventOption(name="volleyball", price_in_uah=100), ChildrenEventOption(name="football", price_in_uah=150), ChildrenEventOption(name="disco", price_in_uah=10), ChildrenEventOption(name="it course", price_in_uah=20)]
    >>> sort_by_price(new_options_list)
    [ChildrenEventOption(venue=EventVenue.MIXED, name=disco, contact_number=, price_in_uah=10, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=it course, contact_number=, price_in_uah=20, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=volleyball, contact_number=, price_in_uah=100, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=football, contact_number=, price_in_uah=150, max_quantity_of_children=0, duration_in_minutes=0)]
    """
    children_events_options_list = sorted(children_events_options_list, key=attrgetter('price_in_uah'))
    if sort_type is SortType.DESCENDING:
        children_events_options_list.reverse()
    return children_events_options_list


def sort_by_name(children_events_options_list: List[ChildrenEventOption], sort_type: SortType = SortType.ASCENDING):
    """
    >>> new_options_list = [ChildrenEventOption(name="volleyball", price_in_uah=100), ChildrenEventOption(name="football", price_in_uah=150), ChildrenEventOption(name="disco", price_in_uah=10), ChildrenEventOption(name="it course", price_in_uah=20)]
    >>> sort_by_name(new_options_list)
    [ChildrenEventOption(venue=EventVenue.MIXED, name=disco, contact_number=, price_in_uah=10, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=football, contact_number=, price_in_uah=150, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=it course, contact_number=, price_in_uah=20, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, name=volleyball, contact_number=, price_in_uah=100, max_quantity_of_children=0, duration_in_minutes=0)]
    """
    children_events_options_list = sorted(children_events_options_list, key=attrgetter('name'))
    if sort_type is SortType.DESCENDING:
        children_events_options_list.reverse()
    return children_events_options_list


if __name__ == '__main__':
    doctest.testmod(verbose=True)

