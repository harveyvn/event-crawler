import re


class Constants:
    def __init__(self):
        self.DOMAIN = "https://www.lucernefestival.ch"
        self.LOCATIONS = "locations"
        self.MONTH = "month"
        self.DAY = "day"
        self.HOUR = "hour"
        self.MINS = "minute"
        self.TITLE = "title"
        self.LINK = "link"
        self.ARTISTS = "artists"
        self.COMPOSERS = "composers"
        self.SONGS = "songs"
        self.PROGRAM = "program"
        self.COVER = "cover"
        self.HTML_TAG = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


CONST = Constants()
