class EventCover:
    def __init__(self, event_id: int, cover_id: int):
        self.event_id = event_id
        self.cover_id = cover_id

    def found(self):
        query = """SELECT * FROM event_covers where event_id = %s and cover_id = %s"""
        items = (self.event_id, self.cover_id,)
        return query, items

    def save(self):
        query = """INSERT INTO  event_covers(event_id, cover_id) VALUES(%s,%s) RETURNING event_id, cover_id;"""
        items = (self.event_id, self.cover_id,)
        return query, items
