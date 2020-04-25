import unittest

from childrenevents.ua.lviv.iot.manager.children_events_options_manager_utils import sort_by_price, sort_by_name
from childrenevents.ua.lviv.iot.model import ChildrenEventOption


class TestChildrenEventsOptionsManagerUtils(unittest.TestCase):

    new_options_list = [ChildrenEventOption(name="volleyball", price_in_uah=100),
                        ChildrenEventOption(name="football", price_in_uah=150),
                        ChildrenEventOption(name="disco", price_in_uah=10),
                        ChildrenEventOption(name="it course", price_in_uah=20)]

    def test_sort_by_name_asc(self):
        new_options_list = sort_by_name(self.new_options_list)
        self.assertEqual(str(new_options_list), '[ChildrenEventOption(venue=EventVenue.MIXED, name=disco, '
                                                'contact_number=, price_in_uah=10, max_quantity_of_children=0, '
                                                'duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, '
                                                'name=football, contact_number=, price_in_uah=150, '
                                                'max_quantity_of_children=0, duration_in_minutes=0), '
                                                'ChildrenEventOption(venue=EventVenue.MIXED, name=it course, '
                                                'contact_number=, price_in_uah=20, max_quantity_of_children=0, '
                                                'duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, '
                                                'name=volleyball, contact_number=, price_in_uah=100, '
                                                'max_quantity_of_children=0, duration_in_minutes=0)]')

    def test_sort_by_price(self):
        new_options_list = sort_by_price(self.new_options_list)
        self.assertEqual(str(new_options_list), '[ChildrenEventOption(venue=EventVenue.MIXED, name=disco, '
                                                'contact_number=, price_in_uah=10, max_quantity_of_children=0, '
                                                'duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, '
                                                'name=it course, contact_number=, price_in_uah=20, '
                                                'max_quantity_of_children=0, duration_in_minutes=0), '
                                                'ChildrenEventOption(venue=EventVenue.MIXED, name=volleyball, '
                                                'contact_number=, price_in_uah=100, max_quantity_of_children=0, '
                                                'duration_in_minutes=0), ChildrenEventOption(venue=EventVenue.MIXED, '
                                                'name=football, contact_number=, price_in_uah=150, '
                                                'max_quantity_of_children=0, duration_in_minutes=0)]')


if __name__ == '__main__':
    unittest.main()
