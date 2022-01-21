import unittest
from snorlax.modules.models import EventSong
from snorlax.modules.constant import CONST


class TestEventSong(unittest.TestCase):
    def test_create_event_song(self):
        a = EventSong(10, 90)
        self.assertEqual((a.event_id, a.song_id), (10, 90))
        b = EventSong("", "")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventSong(10, "90")
        self.assertEqual(b.status, CONST.FAILED)
        b = EventSong("10", 90)
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = EventSong(10, 90)
        self.assertEqual(a.found(), ('SELECT * FROM event_songs where event_id = %s and song_id = %s', (10, 90)))

    def test_check_save_match_query(self):
        a = EventSong(10, 90)
        self.assertEqual(a.save(), ('INSERT INTO  event_songs(event_id, song_id) VALUES(%s,%s) RETURNING event_id, song_id;', (10, 90)))


if __name__ == '__main__':
    unittest.main()
