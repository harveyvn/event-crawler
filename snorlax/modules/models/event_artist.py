class EventArtist:
    def __init__(self, event_id: int, artist_id: int):
        self.event_id = event_id
        self.artist_id = artist_id

    def found(self):
        query = """SELECT * FROM event_artists where event_id = %s and artist_id = %s"""
        items = (self.event_id, self.artist_id,)
        return query, items

    def save(self):
        query = """INSERT INTO  event_artists(event_id, artist_id) VALUES(%s,%s) RETURNING event_id, artist_id;"""
        items = (self.event_id, self.artist_id,)
        return query, items
