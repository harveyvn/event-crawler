import unittest
from modules.models import EventArtist
from modules.constant import CONST


class TestEventArtist(unittest.TestCase):
    def test_create_event_artist(self):
        a = EventArtist(10, 90)
        self.assertEqual((a.event_id, a.artist_id), (10, 90))
        b = EventArtist("", "")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventArtist(10, "90")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventArtist("10", 90)
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = EventArtist(10, 90)
        self.assertEqual(a.found(), ('SELECT * FROM event_artists where event_id = %s and artist_id = %s', (10, 90)))

    def test_check_save_match_query(self):
        a = EventArtist(10, 90)
        self.assertEqual(a.save(), ('INSERT INTO  event_artists(event_id, artist_id) VALUES(%s,%s) RETURNING event_id, artist_id;', (10, 90)))


if __name__ == '__main__':
    unittest.main()
