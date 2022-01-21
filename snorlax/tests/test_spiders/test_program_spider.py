import logging
import unittest

from scrapyscript import Processor, Job

from snorlax.modules.constant import CONST
from snorlax.modules.spiders import ProgramSpider


class TestProgramSpider(unittest.TestCase):
    def test_crawling_event_program(self):
        logging.getLogger("scrapy").propagate = False
        url = "https://www.lucernefestival.ch/en/program/ndr-elbphilharmonie-orchester-ndr-vokalensemble-and-guests-alan-gilbert-louisa-miller-soloists/1777"
        processor = Processor(settings=None)
        job = Job(ProgramSpider, url=url)
        result = processor.run(job)[0]
        self.assertEqual(len(result[CONST.ARTISTS]), 14)
        self.assertEqual(len(result[CONST.SONGS]), 1)

        url = "https://www.lucernefestival.ch/en/program/lucerne-symphony-orchestra-michael-sanderling-joyce-el-khoury/1780"
        processor = Processor(settings=None)
        job = Job(ProgramSpider, url=url)
        result = processor.run(job)[0]
        self.assertEqual(len(result[CONST.ARTISTS]), 3)
        self.assertEqual(len(result[CONST.SONGS]), 3)

    def test_type_of_program_property(self):
        logging.getLogger("scrapy").propagate = False
        url = "https://www.lucernefestival.ch/en/program/ndr-elbphilharmonie-orchester-ndr-vokalensemble-and-guests-alan-gilbert-louisa-miller-soloists/1777"
        processor = Processor(settings=None)
        job = Job(ProgramSpider, url=url)
        result = processor.run(job)[0]
        self.assertEqual(type(result[CONST.ARTISTS]), list)
        self.assertEqual(type(result[CONST.SONGS]), list)

if __name__ == '__main__':
    unittest.main()
