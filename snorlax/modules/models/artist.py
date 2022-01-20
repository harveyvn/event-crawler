class Artist:
    def __init__(self, name: str):
        self.name = name

    def found(self, ):
        query = """SELECT * FROM artists where name = %s"""
        items = (self.name,)
        return query, items

    def save(self):
        query = """INSERT INTO artists(name) VALUES(%s) RETURNING id;"""
        items = (self.name,)
        return query, items
