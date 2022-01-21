from ..constant import CONST


class Song:
    """
    The Song class declares the interface performing on a songs relation.

    Args:
        title (str): A song name.
    """
    def __init__(self, title: str):
        self.title = title
        self.status = CONST.PASSED
        if not title:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return songs rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM songs where title = %s"""
        items = (self.title,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO songs(title) VALUES(%s) RETURNING id;"""
        items = (self.title,)
        return query, items
