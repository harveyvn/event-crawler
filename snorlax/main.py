import logging
from modules import Crawler, Writer

logging.getLogger("scrapy").propagate = False

if __name__ == '__main__':
    urls = ["https://www.lucernefestival.ch/en/program/summer-festival-22",
            "https://www.lucernefestival.ch/en/program/mendelssohn-festival-22"]

    crawler = Crawler(urls[0])

    writer = Writer(events=crawler.events)
    writer.to_db()

