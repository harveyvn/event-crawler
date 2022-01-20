import scrapy
import re
from ..constant import CONST
from ..common import generate, is_numeric, is_empty


class EventSpider(scrapy.spiders.Spider):
    name = "events"

    def start_requests(self):
        yield scrapy.Request(self.url)

    @staticmethod
    def validate(day, month, hour, minute, locations, title, link, cover):
        if is_numeric([day, month, hour, minute]) is False:
            return False

        if len(locations) == 0:
            return False

        if is_empty([title, link, cover]) is False:
            return False

        return True

    def parse(self, response):
        # Define css selectors
        day_sel = "//div[@class='entry']/div[@class='wi']/div[@class='date-place']/div[@class='left']/p[@class='date']/text()"
        month_sel = "//div[@class='entry']/div[@class='wi']/div[@class='date-place']/div[@class='left']/p[@class='month-number']/text()"
        time_sel = "//div[@class='entry']/div[@class='wi']/div[@class='date-place']/div[@class='right']/p[@class='day-time']/span[@class='time']/text()"
        location_sel = "//div[@class='entry']/div[@class='wi']/div[@class='date-place']/p[@class='location']"
        title_sel = "//div[@class='entry']/div[@class='wi']/div[@class='event-info']/div[@class='wi']/p[@class='surtitle']/text()"
        link_sel = "//div[@class='entry']/div[@class='wi']/div[@class='event-info']/div[@class='wi']/p[@class='title']/a/@href"
        cover_sel = "//div[@class='entry']/div[@class='wi']/div[@class='image']/@style"

        # Extract the items
        locations = generate(response, location_sel)
        days = generate(response, day_sel)
        months = generate(response, month_sel)
        times = generate(response, time_sel)
        titles = generate(response, title_sel)
        links = generate(response, link_sel)
        covers = generate(response, cover_sel)

        # Assure the number of each properties are equal
        assert len(locations) == len(days) == len(months) == len(times) == len(titles) == len(links) == len(covers)

        events = []
        for locations, day, month, time, title, link, cover \
                in zip(locations, days, months, times, titles, links, covers):
            day = day.replace('.', '')
            month = month.replace('.', '')
            hour, minute = time.split('.')
            locations = re.sub(CONST.HTML_TAG, '', locations)
            locations = re.sub("\s+", '', locations).split(',')
            cover = re.findall(r'\((.*?)\)', cover)
            link = CONST.DOMAIN + link
            title = title.title()
            if self.validate(day, month, hour, minute, locations, title, link, cover):
                event = {
                    CONST.DAY: int(day),
                    CONST.MONTH: int(month),
                    CONST.HOUR: int(hour),
                    CONST.MINS: int(minute),
                    CONST.LOCATIONS: locations,
                    CONST.TITLE: title,
                    CONST.LINK: link,
                    CONST.COVER: cover
                }
                events.append(event)
        return events
