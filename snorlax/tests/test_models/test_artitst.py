import unittest
from snorlax.modules.models import Artist
from snorlax.modules.constant import CONST


class TestArtist(unittest.TestCase):
    def test_create_artist(self):
        a = Artist("Pokemon")
        b = Artist("")

        self.assertEqual(a.name, "Pokemon")
        self.assertEqual(a.status, CONST.PASSED)
        self.assertEqual(b.name, "")
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = Artist("Pokemon")
        self.assertEqual(a.found(), ('SELECT * FROM artists where name = %s', ('Pokemon',)))

    def test_check_save_match_query(self):
        a = Artist("Pokemon")
        self.assertEqual(a.save(), ('INSERT INTO artists(name) VALUES(%s) RETURNING id;', ('Pokemon',)))


if __name__ == '__main__':
    unittest.main()
