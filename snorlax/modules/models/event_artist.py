from ..constant import CONST


class EventArtist:
    """
    The EventArtist class declares the interface performing on an event_artists relation.

    Args:
        event_id (int): An event ID.
        artist_id (int): An artist ID.
    """
    def __init__(self, event_id: int, artist_id: int):
        self.event_id = event_id
        self.artist_id = artist_id
        self.status = CONST.PASSED
        if type(event_id) != int or type(artist_id) != int:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return event_artists rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM event_artists where event_id = %s and artist_id = %s"""
        items = (self.event_id, self.artist_id,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO  event_artists(event_id, artist_id) VALUES(%s,%s) RETURNING event_id, artist_id;"""
        items = (self.event_id, self.artist_id,)
        return query, items
