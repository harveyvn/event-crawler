import logging
import unittest

from scrapyscript import Processor, Job

from modules.constant import CONST
from modules.spiders import EventSpider


class TestEventSpider(unittest.TestCase):
    def test_crawling_events(self):
        logging.getLogger("scrapy").propagate = False
        url = "https://www.lucernefestival.ch/en/program/mendelssohn-festival-22"
        processor = Processor(settings=None)
        job = Job(EventSpider, url=url)
        events = processor.run(job)

        # There are 3 events
        self.assertEqual(len(events), 3)

    def test_type_of_event_property(self):
        logging.getLogger("scrapy").propagate = False
        url = "https://www.lucernefestival.ch/en/program/mendelssohn-festival-22"
        processor = Processor(settings=None)
        job = Job(EventSpider, url=url)
        events = processor.run(job)

        for event in events:
            self.assertEqual(type(event[CONST.DATE]), str)
            self.assertEqual(type(event[CONST.HOUR]), int)
            self.assertEqual(type(event[CONST.MINS]), int)
            self.assertEqual(type(event[CONST.LOCATIONS]), list)
            self.assertGreater(len(event[CONST.LOCATIONS]), 0)
            self.assertEqual(type(event[CONST.LINK]), str)
            self.assertEqual(type(event[CONST.COVER]), str)


if __name__ == '__main__':
    unittest.main()
