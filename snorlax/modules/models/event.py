from ..constant import CONST


class Event:
    """
    The Event class declares the interface performing on an events relation.

    Args:
        title (str): An event name.
    """
    def __init__(self, title: str):
        self.title = title
        self.status = CONST.PASSED
        if not title:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return events rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM events where title = %s"""
        items = (self.title,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO events(title) VALUES(%s) RETURNING id;"""
        items = (self.title,)
        return query, items
