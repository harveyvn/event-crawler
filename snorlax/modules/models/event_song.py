from ..constant import CONST


class EventSong:
    """
    The EventSong class declares the interface performing on an event_songs relation.

    Args:
        event_id (int): An event ID.
        song_id (int): A song ID.
    """

    def __init__(self, event_id: int, song_id: int):
        self.event_id = event_id
        self.song_id = song_id
        self.status = CONST.PASSED
        if type(event_id) != int or type(song_id) != int:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return event_songs rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM event_songs where event_id = %s and song_id = %s"""
        items = (self.event_id, self.song_id,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO  event_songs(event_id, song_id) VALUES(%s,%s) RETURNING event_id, song_id;"""
        items = (self.event_id, self.song_id,)
        return query, items
