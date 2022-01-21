import logging
import unittest
from modules.controllers import Crawler
from modules.constant import CONST


class TestCrawler(unittest.TestCase):
    def test_crawler_get_events_programs(self):
        logging.getLogger("scrapy").propagate = False
        events = Crawler("https://www.lucernefestival.ch/en/program/mendelssohn-festival-22").events

        self.assertEqual(len(events), 3)  # add assertion here
        for event in events:
            self.assertEqual(type(event[CONST.DATE]), str)
            self.assertEqual(type(event[CONST.HOUR]), int)
            self.assertEqual(type(event[CONST.MINS]), int)
            self.assertEqual(type(event[CONST.LOCATIONS]), list)
            self.assertGreater(len(event[CONST.LOCATIONS]), 0)
            self.assertEqual(type(event[CONST.LINK]), str)
            self.assertEqual(type(event[CONST.COVER]), str)
            self.assertEqual(type(event[CONST.PROGRAM][CONST.ARTISTS]), list)
            self.assertEqual(type(event[CONST.PROGRAM][CONST.SONGS]), list)
            self.assertGreater(len(event[CONST.PROGRAM][CONST.ARTISTS]), 0)
            self.assertGreater(len(event[CONST.PROGRAM][CONST.SONGS]), 0)


if __name__ == '__main__':
    unittest.main()
