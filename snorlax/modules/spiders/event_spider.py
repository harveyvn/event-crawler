import scrapy
import re
from ..constant import CONST
from ..common import generate, is_numeric, is_empty


class EventSpider(scrapy.spiders.Spider):
    """
    The EventSpider class declares the interface that crawls events from given url.

    """
    name = "events"

    def start_requests(self):
        yield scrapy.Request(self.url)

    @staticmethod
    def validate(date, hour, minute, locations, title, link, cover):
        """
        Validate type and information content for each event's property.
        - date (str): not null
        - hour(int): numeric
        - minutes (int): numeric
        - location (list): at least one city
        - title (str): an event name - not null
        - link (str): an event url to crawl its programs, artists and songs - not null
        - cover (str): an event cover image's url - not null

        Returns: Boolean
        """
        if is_numeric([hour, minute]) is False:
            return False

        if len(locations) == 0:
            return False

        if is_empty([title, link, cover, date]) is False:
            return False

        return True

    def parse(self, response):
        """
        Define appropriate css selectors, then use them to guide a spider crawling useful text
        from corresponding html sections.

        Returns:
            [dict]: A list of event dictionaries, each event dictionary consists of:
                    - date (str)
                    - hour(int)
                    - minutes (int)
                    - location (list): cities host an events
                    - title (str): an event name
                    - link (str): an event url to crawl its programs, artists and songs
                    - cover (str): an event cover image's url
        """
        # Define css selectors
        date_sel = "//div[@class='entry']/@data-date"
        time_sel = "//div[@class='entry']/div[@class='wi']/div[@class='date-place']/div[@class='right']/p[@class='day-time']/span[@class='time']/text()"
        location_sel = "//div[@class='entry']/div[@class='wi']/div[@class='date-place']/p[@class='location']"
        title_sel = "//div[@class='entry']/div[@class='wi']/div[@class='event-info']/div[@class='wi']/p[@class='surtitle']/text()"
        link_sel = "//div[@class='entry']/div[@class='wi']/div[@class='event-info']/div[@class='wi']/p[@class='title']/a/@href"
        cover_sel = "//div[@class='entry']/div[@class='wi']/div[@class='image']/@style"

        # Extract the items
        locations = generate(response, location_sel)
        dates = generate(response, date_sel)
        times = generate(response, time_sel)
        titles = generate(response, title_sel)
        links = generate(response, link_sel)
        covers = generate(response, cover_sel)

        # Assure the number of each properties are equal
        if not (len(locations) == len(dates) == len(times) == len(titles) == len(links) == len(covers)):
            return []

        # Clean the extracted content
        events = []
        for locations, date, time, title, link, cover \
                in zip(locations, dates, times, titles, links, covers):
            hour, minute = time.split('.')
            locations = re.sub(CONST.HTML_TAG, '', locations)
            locations = re.sub("\t", '', locations)
            locations = [location.lstrip() for location in re.sub("\n", '', locations).split(',')]
            cover = re.findall(r'\((.*?)\)', cover)[0]
            link = CONST.DOMAIN + link
            title = title.title()
            if self.validate(date, hour, minute, locations, title, link, cover):
                event = {
                    CONST.DATE: date,
                    CONST.HOUR: int(hour),
                    CONST.MINS: int(minute),
                    CONST.LOCATIONS: locations,
                    CONST.TITLE: title,
                    CONST.LINK: link,
                    CONST.COVER: cover
                }
                events.append(event)
        return events
