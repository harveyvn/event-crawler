import unittest
from modules.models import EventLocation
from modules.constant import CONST


class TestEventLocation(unittest.TestCase):
    def test_create_event_location(self):
        a = EventLocation(10, 90, "2022-10-19 10:23:54+02")
        self.assertEqual((a.event_id, a.location_id, a.date), (10, 90, "2022-10-19 10:23:54+02"))
        b = EventLocation("", "", "")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventLocation(10, "90", "2022-10-19 10:23:54+02")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventLocation("10", 90, "2022-10-19 10:23:54+02")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventLocation(10, 90, "")
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = EventLocation(10, 90, "2022-10-19 10:23:54+02")
        self.assertEqual(a.found(), ('SELECT * FROM event_locations where event_id = %s and location_id = %s', (10, 90)))

    def test_check_save_match_query(self):
        a = EventLocation(10, 90, "2022-10-19 10:23:54+02")
        self.assertEqual(a.save(), ('INSERT INTO  event_locations(event_id, location_id, date) VALUES(%s,%s,%s) RETURNING event_id, location_id;', (10, 90, "2022-10-19 10:23:54+02")))


if __name__ == '__main__':
    unittest.main()
