import unittest
from snorlax.modules.models import Location
from snorlax.modules.constant import CONST


class TestLocation(unittest.TestCase):
    def test_create_location(self):
        a = Location("Berlin")
        b = Location("")

        self.assertEqual(a.name, "Berlin")
        self.assertEqual(a.status, CONST.PASSED)
        self.assertEqual(b.name, "")
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = Location("Berlin")
        self.assertEqual(a.found(), ('SELECT * FROM locations where name = %s', ('Berlin',)))

    def test_check_save_match_query(self):
        a = Location("Berlin")
        self.assertEqual(a.save(), ('INSERT INTO locations(name) VALUES(%s) RETURNING id;', ('Berlin',)))


if __name__ == '__main__':
    unittest.main()
