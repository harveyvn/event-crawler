import psycopg2
from typing import List
from yaspin import yaspin
from modules.constant import CONST
from modules.connection import Connection
from modules.common import timestamp
from modules.models import Location, Cover, Artist, Song, Event, EventLocation, EventCover, EventArtist, EventSong


class Writer:
    def __init__(self, events: List[dict]):
        self.events = events
        self.event_ids = []

    def to_db(self):
        events = self.events
        conn = None
        with yaspin(text="Writing an event to db!", color="yellow") as spinner:
            try:
                print("\nConnecting to the PostgreSQl database...")
                conn = Connection()
                print(f'PostgreSQl database version: {conn.exec_select("SELECT version()")}')
                for idx, event in enumerate(events):
                    event_id = conn.process(Event(title=event[CONST.TITLE]))
                    if event_id == CONST.FAILED:
                        continue

                    date = timestamp(event[CONST.DATE], event[CONST.HOUR], event[CONST.MINS])

                    cover_id = conn.process(Cover(url=event[CONST.COVER]))
                    if cover_id > CONST.FAILED:
                        conn.process(EventCover(event_id, cover_id))

                    if event_id > CONST.FAILED:
                        for location in event[CONST.LOCATIONS]:
                            location_id = conn.process(Location(name=location))
                            if location_id > CONST.FAILED:
                                conn.process(EventLocation(event_id, location_id, date))

                        for artist in event[CONST.PROGRAM][CONST.ARTISTS]:
                            artist_id = conn.process(Artist(name=artist))
                            if artist_id > CONST.FAILED:
                                conn.process(EventArtist(event_id, artist_id))

                        for song in event[CONST.PROGRAM][CONST.SONGS]:
                            song_id = conn.process(Song(title=song))
                            if song_id > CONST.FAILED:
                                conn.process(EventSong(event_id, song_id))

                    self.event_ids.append(event_id)
                    spinner.ok(f'✅ Done event {idx}!')

            except(Exception, psycopg2.DatabaseError) as e:
                spinner.fail(f'💥 Exception! {e}')
            finally:
                if conn is not None:
                    conn.close()
                    print("Database connection closed.")
