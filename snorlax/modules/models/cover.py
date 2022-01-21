from ..constant import CONST


class Cover:
    """
    The Cover class declares the interface performing on a covers relation.

    Args:
        url (str): A cover image url.
    """
    def __init__(self, url: str):
        self.url = url
        self.status = CONST.PASSED
        if not url:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return covers rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM covers where url = %s"""
        items = (self.url,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO covers(url) VALUES(%s) RETURNING id;"""
        items = (self.url,)
        return query, items
