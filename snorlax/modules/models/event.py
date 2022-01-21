from ..constant import CONST


class Event:
    def __init__(self, title: str):
        self.title = title
        self.status = CONST.PASSED
        if not title:
            self.status = CONST.FAILED

    def found(self):
        query = """SELECT * FROM events where title = %s"""
        items = (self.title,)
        return query, items

    def save(self):
        query = """INSERT INTO events(title) VALUES(%s) RETURNING id;"""
        items = (self.title,)
        return query, items
