import scrapy
import re
from ..constant import CONST
from ..common import generate


class ProgramSpider(scrapy.spiders.Spider):
    name = "program"

    def start_requests(self):
        yield scrapy.Request(self.url)

    @staticmethod
    def validate(artists, songs):
        if len(artists) < 1 or len(songs) < 1:
            return False
        return True

    def parse(self, response):
        # Define css selector
        artist_sel = "//div[@class='artists-musical-pieces']/div[@class='artist']/strong"
        song_sel = "//div[@class='artists-musical-pieces']/div[@class='musical-piece']"
        song_sel_alt = "//div[@class='artists-musical-pieces']/div[@class='with-spaces']"

        artists = [re.sub(CONST.HTML_TAG, '', artist).strip() for artist in generate(response, artist_sel)]
        songs = generate(response, song_sel) if len(generate(response, song_sel)) > 0 else generate(response, song_sel_alt)
        for i, song in enumerate(songs):
            songs[i] = re.sub(CONST.HTML_TAG, '', songs[i]).strip()
            songs[i] = re.sub(r'\xa0', '', songs[i])
            songs[i] = re.sub(r'“', '', songs[i])
            songs[i] = re.sub(r'”', ' ', songs[i])
            songs[i] = re.sub(r'\t', '', songs[i])
            songs[i] = re.sub(r'\n', '', songs[i])
            songs[i] = re.sub(r'\r', '', songs[i])
            songs[i] = re.sub(r'-->', '', songs[i])
            songs[i] = re.sub(r'\)', ') ', songs[i])
            songs[i] = ' '.join([x.title() for x in songs[i].split(' ') if x])

        if self.validate(artists, songs) is True:
            return {
                CONST.ARTISTS: artists,
                CONST.SONGS: songs
            }
        pass
