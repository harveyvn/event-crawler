import unittest
from snorlax.modules.models import EventCover
from snorlax.modules.constant import CONST


class TestEventCover(unittest.TestCase):
    def test_create_event_cover(self):
        a = EventCover(10, 90)
        self.assertEqual((a.event_id, a.cover_id), (10, 90))
        b = EventCover("", "")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventCover(10, "90")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventCover("10", 90)
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = EventCover(10, 90)
        self.assertEqual(a.found(), ('SELECT * FROM event_covers where event_id = %s and cover_id = %s', (10, 90)))

    def test_check_save_match_query(self):
        a = EventCover(10, 90)
        self.assertEqual(a.save(), ('INSERT INTO  event_covers(event_id, cover_id) VALUES(%s,%s) RETURNING event_id, cover_id;', (10, 90)))


if __name__ == '__main__':
    unittest.main()
