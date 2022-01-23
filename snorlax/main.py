from __future__ import print_function, unicode_literals
import logging
from modules.controllers import Crawler, Writer, Uploader

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

                    print("(Y) Download as csv file, (Q) Quit, (Others) Back to welcome screen.")
                    choice = input("Choice: ")
                    if choice == 'Y':
                        Uploader.write_file()
                        print(f'Download demo.csv at: {Uploader.upload_file()}')
                    if choice == 'Q':
                        flag = False
                elif choice == 'Q':
                    flag = False
