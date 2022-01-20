class Cover:
    def __init__(self, url: str):
        self.url = url

    def found(self):
        query = """SELECT * FROM covers where url = %s"""
        items = (self.url,)
        return query, items

    def save(self):
        query = """INSERT INTO covers(url) VALUES(%s) RETURNING id;"""
        items = (self.url,)
        return query, items
