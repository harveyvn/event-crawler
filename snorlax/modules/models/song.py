class Song:
    def __init__(self, title: str):
        self.title = title

    def found(self):
        query = """SELECT * FROM songs where title = %s"""
        items = (self.title,)
        return query, items

    def save(self):
        query = """INSERT INTO songs(title) VALUES(%s) RETURNING id;"""
        items = (self.title,)
        return query, items
