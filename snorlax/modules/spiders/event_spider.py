import scrapy
import re
from ..constant import CONST
from ..common import generate, is_numeric, is_empty


class EventSpider(scrapy.spiders.Spider):
    name = "events"

    def start_requests(self):
        yield scrapy.Request(self.url)

    @staticmethod
    def validate(date, hour, minute, locations, title, link, cover):
        if is_numeric([hour, minute]) is False:
            return False

        if not date:
            return False

        if len(locations) == 0:
            return False

        if is_empty([title, link, cover]) is False:
            return False

        return True

    def parse(self, response):
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
        assert len(locations) == len(dates) == len(times) == len(titles) == len(links) == len(covers)

        events = []
        for locations, date, time, title, link, cover \
                in zip(locations, dates, times, titles, links, covers):
            hour, minute = time.split('.')
            locations = re.sub(CONST.HTML_TAG, '', locations)
            locations = re.sub("\t", '', locations)
            locations = [location.lstrip() for location in re.sub("\n", '', locations).split(',')]
            cover = re.findall(r'\((.*?)\)', cover)
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
