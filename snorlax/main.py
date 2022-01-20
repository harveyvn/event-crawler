import logging
import psycopg2
from modules import CONST, Connection, Crawler
from modules.models import Location, Cover

logging.getLogger("scrapy").propagate = False

if __name__ == '__main__':
    urls = ["https://www.lucernefestival.ch/en/program/summer-festival-22",
            "https://www.lucernefestival.ch/en/program/mendelssohn-festival-22"]

    crawler = Crawler(urls[0])
    crawler.get_events()
    crawler.get_programs()

    events = crawler.events

    conn = None
    try:
        print("Connecting to the PostgreSQl database...")
        conn = Connection()
        print(f'PostgreSQl database version: {conn.exec_select("SELECT version()")}')

        for event in events:
            for location in event[CONST.LOCATIONS]:
                conn.process(Location(name=location))
            for cover in event[CONST.COVER]:
                print(conn.process(Cover(url=cover)))

    except(Exception, psycopg2.DatabaseError) as e:
        print("Exception:", e)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")
