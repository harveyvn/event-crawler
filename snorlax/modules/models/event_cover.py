from ..constant import CONST


class EventCover:
    """
    The EventCover class declares the interface performing on an event_covers relation.

    Args:
        event_id (int): An event ID.
        cover_id (int): A cover ID.
    """
    def __init__(self, event_id: int, cover_id: int):
        self.event_id = event_id
        self.cover_id = cover_id
        self.status = CONST.PASSED
        if type(event_id) != int or type(cover_id) != int:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return event_covers rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM event_covers where event_id = %s and cover_id = %s"""
        items = (self.event_id, self.cover_id,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO  event_covers(event_id, cover_id) VALUES(%s,%s) RETURNING event_id, cover_id;"""
        items = (self.event_id, self.cover_id,)
        return query, items
