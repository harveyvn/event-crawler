from modules.connection import Connection


class Reader:
    """
    The Reader class declares the interface that extract information by given event_id.
    """
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = Connection()

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def get_date(self, id):
        """
        Get an event date.
        Args:
            id (int): an event id.
        Return:
            date (str): an event date.
        """
        self.conn.cur.execute(f'SELECT DISTINCT b."date" FROM event_locations b, locations c WHERE b.event_id = {id} AND b.location_id = c.id;')
        return self.conn.cur.fetchall()[0][0]

    def get_cover(self, id):
        """
        Get an event cover.
        Args:
            id (int): an event id.
        Return:
            title (str): an event cover.
        """
        self.conn.cur.execute(f'SELECT c."url" FROM event_covers b, covers c WHERE b.event_id = {id} AND b.cover_id = c.id;')
        return self.conn.cur.fetchall()[0][0]

    def get_title(self, id):
        """
        Get an event title.
        Args:
            id (int): an event id.
        Return:
            title (str): an event title.
        """
        self.conn.cur.execute(f'SELECT title FROM events WHERE id={id};')
        return self.conn.cur.fetchall()[0][0]

    def get_artists(self, id):
        """
        Get an event title.
        Args:
            id (int): an event id.
        Return:
            artists ([str]): an event' artists.
        """
        self.conn.cur.execute(f'SELECT DISTINCT c."name" FROM event_artists b, artists c WHERE b.event_id = {id} AND b.artist_id = c.id;')
        return [artist[0] for artist in self.conn.cur.fetchall()]

    def get_locations(self, id):
        """
        Get an event' locations.
        Args:
            id (int): an event id.
        Return:
            locations ([str]): an event' locations.
        """
        self.conn.cur.execute(f'SELECT DISTINCT c."name" FROM event_locations b, locations c WHERE b.event_id = {id} AND b.location_id = c.id;')
        return [location[0] for location in self.conn.cur.fetchall()]

    def get_songs(self, id):
        """
        Get an event' songs.
        Args:
            id (int): an event id.
        Return:
            songs ([str]): an event' songs.
        """
        self.conn.cur.execute(f'SELECT DISTINCT c.title FROM event_songs b, songs c WHERE b.event_id = {id} AND b.song_id = c.id;')
        return [song[0] for song in self.conn.cur.fetchall()]