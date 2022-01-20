import scrapy
import re
from ..constant import CONST
from ..common import generate_items


class ProgramSpider(scrapy.spiders.Spider):
    name = "program"

    def start_requests(self):
        yield scrapy.Request(self.url)

    def parse(self, response):
        # Define css selector
        artist_sel = "//div[@class='artists-musical-pieces']/div[@class='artist']/strong"
        song_sel = "//div[@class='artists-musical-pieces']/div[@class='musical-piece']"
        song_sel_alt = "//div[@class='artists-musical-pieces']/div[@class='with-spaces']"

        artists = [re.sub(CONST.HTML_TAG, '', artist).strip() for artist in generate_items(response, artist_sel)]
        songs = generate_items(response, song_sel)
        if len(songs) == 0:
            songs = generate_items(response, song_sel_alt)
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

        assert len(artists) > 0
        assert len(songs) > 0

        return {
            CONST.ARTISTS: artists,
            CONST.SONGS: songs
        }

