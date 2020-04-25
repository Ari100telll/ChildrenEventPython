import unittest

from childrenevents.ua.lviv.iot.manager.children_events_options_manager import ChildrenEventsOptionsManager
from childrenevents.ua.lviv.iot.model import ChildrenEventOption


class TestChildrenEventsOptionsManager(unittest.TestCase):

    def test_find_option_by_criterion(self):
        manager = ChildrenEventsOptionsManager([ChildrenEventOption(name="volleyball", price_in_uah=100),
                                                ChildrenEventOption(name="football", price_in_uah=150),
                                                ChildrenEventOption(name="disco", price_in_uah=10),
                                                ChildrenEventOption(name="it course", price_in_uah=20)])
        self.assertEqual(str(manager.find_option_by_criterion(max_price_in_uah=100)),
                         '[ChildrenEventOption(venue=EventVenue.MIXED, name=volleyball, contact_number=, '
                         'price_in_uah=100, max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption('
                         'venue=EventVenue.MIXED, name=disco, contact_number=, price_in_uah=10, '
                         'max_quantity_of_children=0, duration_in_minutes=0), ChildrenEventOption('
                         'venue=EventVenue.MIXED, name=it course, contact_number=, price_in_uah=20, '
                         'max_quantity_of_children=0, duration_in_minutes=0)]')


if __name__ == '__main__':
    unittest.main()
