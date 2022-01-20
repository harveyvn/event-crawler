class Location:
    def __init__(self, name: str):
        self.name = name

    def found(self, ):
        query = """SELECT * FROM locations where name = %s"""
        items = (self.name,)
        return query, items

    def save(self):
        query = """INSERT INTO locations(name) VALUES(%s) RETURNING id;"""
        items = (self.name,)
        return query, items
