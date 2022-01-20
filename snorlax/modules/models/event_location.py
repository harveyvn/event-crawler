class EventLocation:
    def __init__(self, event_id: int, location_id: int, date: str):
        self.event_id = event_id
        self.location_id = location_id
        self.date = date

    def found(self, ):
        query = """SELECT * FROM event_locations where event_id = %s and location_id = %s"""
        items = (self.event_id, self.location_id,)
        return query, items

    def save(self):
        query = """INSERT INTO  event_locations(event_id, location_id, date) VALUES(%s,%s,%s) RETURNING event_id, location_id;"""
        items = (self.event_id, self.location_id, self.date,)
        return query, items
