class EventSong:
    def __init__(self, event_id: int, song_id: int):
        self.event_id = event_id
        self.song_id = song_id

    def found(self):
        query = """SELECT * FROM event_songs where event_id = %s and song_id = %s"""
        items = (self.event_id, self.song_id,)
        return query, items

    def save(self):
        query = """INSERT INTO  event_songs(event_id, song_id) VALUES(%s,%s) RETURNING event_id, song_id;"""
        items = (self.event_id, self.song_id,)
        return query, items
