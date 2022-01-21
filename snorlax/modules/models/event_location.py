from ..constant import CONST


class EventLocation:
    """
    The EventLocation class declares the interface performing on an event_locations relation.

    Args:
        event_id (int): An event ID.
        location_id (int): A cover ID.
        date (str): Date and time of an event.
    """
    def __init__(self, event_id: int, location_id: int, date: str):
        self.event_id = event_id
        self.location_id = location_id
        self.date = date
        self.status = CONST.PASSED
        if type(event_id) != int or type(location_id) != int or not date:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return event_locations rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM event_locations where event_id = %s and location_id = %s"""
        items = (self.event_id, self.location_id,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO  event_locations(event_id, location_id, date) VALUES(%s,%s,%s) RETURNING event_id, location_id;"""
        items = (self.event_id, self.location_id, self.date,)
        return query, items
