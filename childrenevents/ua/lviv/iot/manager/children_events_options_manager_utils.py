from operator import attrgetter
from typing import List

from childrenevents.ua.lviv.iot.model import ChildrenEventOption
from childrenevents.ua.lviv.iot.model.sort_type import SortType


def sort_by_price(children_events_options_manager: List[ChildrenEventOption], sort_type: SortType):
    children_events_options_manager = sorted(children_events_options_manager, key=attrgetter('price_in_uah'))
    if sort_type is SortType.DESCENDING:
        children_events_options_manager.reverse()


def sort_by_name(children_events_options_manager: List[ChildrenEventOption], sort_type: SortType):
    children_events_options_manager = sorted(children_events_options_manager,
                                             key=attrgetter('name'))
    if sort_type is SortType.DESCENDING:
        children_events_options_manager.reverse()
