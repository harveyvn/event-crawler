import unittest
from snorlax.modules.models import Event
from snorlax.modules.constant import CONST


class TestEvent(unittest.TestCase):
    def test_create_event(self):
        a = Event("Pokemon")
        b = Event("")

        self.assertEqual(a.title, "Pokemon")
        self.assertEqual(a.status, CONST.PASSED)
        self.assertEqual(b.title, "")
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = Event("Pokemon")
        self.assertEqual(a.found(), ('SELECT * FROM events where title = %s', ('Pokemon',)))

    def test_check_save_match_query(self):
        a = Event("Pokemon")
        self.assertEqual(a.save(), ('INSERT INTO events(title) VALUES(%s) RETURNING id;', ('Pokemon',)))


if __name__ == '__main__':
    unittest.main()
