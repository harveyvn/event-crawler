import psycopg2
from typing import List
from yaspin import yaspin
from .constant import CONST
from .connection import Connection
from .common import timestamp
from .models import Location, Cover, Artist, Song, Event, EventLocation, EventCover, EventArtist, EventSong


class Writer:
    def __init__(self, events: List[dict]):
        self.events = events

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
                    date = timestamp(event[CONST.DATE], event[CONST.HOUR], event[CONST.MINS])

                    for location in event[CONST.LOCATIONS]:
                        location_id = conn.process(Location(name=location))
                        conn.process(EventLocation(event_id, location_id, date))

                    for cover in event[CONST.COVER]:
                        cover_id = conn.process(Cover(url=cover))
                        conn.process(EventCover(event_id, cover_id))

                    for artist in event[CONST.PROGRAM][CONST.ARTISTS]:
                        artist_id = conn.process(Artist(name=artist))
                        conn.process(EventArtist(event_id, artist_id))

                    for song in event[CONST.PROGRAM][CONST.SONGS]:
                        song_id = conn.process(Song(title=song))
                        conn.process(EventSong(event_id, song_id))

                    spinner.ok(f'✅ Done event {idx}!')

            except(Exception, psycopg2.DatabaseError) as e:
                spinner.fail(f'💥 Exception! {e}')
            finally:
                if conn is not None:
                    conn.close()
                    print("Database connection closed.")
