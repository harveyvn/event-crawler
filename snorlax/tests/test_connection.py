import logging
import unittest
import psycopg2

from modules.crawler import Crawler
from modules.constant import CONST
from modules.connection import Connection
from modules.models import Event


class TestConnection(unittest.TestCase):
    def test_establish_connection(self):
        conn = None
        try:
            conn = Connection()
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            self.assertEqual(True, False)
        finally:
            if conn is not None:
                conn.close()
                self.assertEqual(True, True)

    def test_exec_process(self):
        logging.getLogger("scrapy").propagate = False
        events = Crawler("https://www.lucernefestival.ch/en/program/mendelssohn-festival-22").events
        conn = None
        try:
            conn = Connection()
            for idx, event in enumerate(events):
                event_id = conn.process(Event(title=event[CONST.TITLE]))
                self.assertGreater(event_id, -1)
                event_id = conn.process(Event(title=""))
                self.assertEqual(event_id, -1)
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            self.assertEqual(True, False)
        finally:
            if conn is not None:
                conn.close()
                self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
