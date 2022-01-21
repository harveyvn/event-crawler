from __future__ import print_function, unicode_literals
import logging
from modules import Crawler, Writer

logging.getLogger("scrapy").propagate = False

if __name__ == '__main__':
    urls = ["https://www.lucernefestival.ch/en/program/summer-festival-22",
            "https://www.lucernefestival.ch/en/program/mendelssohn-festival-22"]

    flag = True
    while flag:
        print("Welcome to simple crawler! (Y) Continue, (Q) Quit.")
        choice = input("Choice: ")
        if choice == 'Q':
            flag = False
        if choice == 'T':
            pass
        if choice == 'Y':
            url = input("Enter an url to crawl events, (B) Back: ")
            if url == 'B':
                pass
            else:
                events = Crawler(url).events

                print("(Y) Write to db, (Q) Quit, (Others) Back to welcome screen.")
                choice = input("Choice: ")
                if choice == 'Y':
                    Writer(events=events).to_db()
                elif choice == 'Q':
                    flag = False
