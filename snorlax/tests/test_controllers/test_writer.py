import logging
import unittest
from dateutil.parser import parse
from modules.constant import CONST
from modules.common import timestamp
from modules.controllers import Writer, Reader, Crawler


class TestWriter(unittest.TestCase):
    def test_writer_write_an_event_to_db(self):
        logging.getLogger("scrapy").propagate = False
        events = Crawler("https://www.lucernefestival.ch/en/program/mendelssohn-festival-22").events

        writer = Writer([events[0]])
        writer.to_db()
        event_ids = writer.event_ids

        reader = Reader()
        reader.connect()

        id = event_ids[0]
        event = events[0]
        self.assertEqual(event[CONST.TITLE], reader.get_title(id))
        self.assertEqual(event[CONST.COVER], reader.get_cover(id))
        d1 = parse(str(reader.get_date(id))).utctimetuple()
        d2 = parse(timestamp(event[CONST.DATE], event[CONST.HOUR], event[CONST.MINS])).utctimetuple()
        self.assertEqual(d1, d2)
        self.assertEqual(sorted(reader.get_locations(id)), sorted(list(set(event[CONST.LOCATIONS]))))
        self.assertEqual(sorted(reader.get_artists(id)), sorted(list(set(event[CONST.PROGRAM][CONST.ARTISTS]))))
        self.assertEqual(sorted(reader.get_songs(id)), sorted(list(set(event[CONST.PROGRAM][CONST.SONGS]))))

    def test_writer_write_an_invalid_event_to_db(self):
        logging.getLogger("scrapy").propagate = False
        event = {
            CONST.DATE: None,
            CONST.HOUR: None,
            CONST.MINS: None,
            CONST.LOCATIONS: [],
            CONST.TITLE: None,
            CONST.LINK: None,
            CONST.COVER: None
        }
        writer = Writer([event])
        writer.to_db()
        event_ids = writer.event_ids
        self.assertEqual(len(event_ids), 0)


if __name__ == '__main__':
    unittest.main()
