import unittest
from snorlax.modules.models import Song
from snorlax.modules.constant import CONST


class TestSong(unittest.TestCase):
    def test_create_song(self):
        a = Song("Pokemon")
        b = Song("")

        self.assertEqual(a.title, "Pokemon")
        self.assertEqual(a.status, CONST.PASSED)
        self.assertEqual(b.title, "")
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = Song("Pokemon")
        self.assertEqual(a.found(), ('SELECT * FROM songs where title = %s', ('Pokemon',)))

    def test_check_save_match_query(self):
        a = Song("Pokemon")
        self.assertEqual(a.save(), ('INSERT INTO songs(title) VALUES(%s) RETURNING id;', ('Pokemon',)))


if __name__ == '__main__':
    unittest.main()
