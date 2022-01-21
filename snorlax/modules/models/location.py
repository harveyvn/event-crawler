from ..constant import CONST


class Location:
    """
    The Location class declares the interface performing on a locations relation.

    Args:
        name (str): Location name.
    """
    def __init__(self, name: str):
        self.name = name
        self.status = CONST.PASSED
        if not name:
            self.status = CONST.FAILED

    def found(self):
        """
        Generate a select query to return locations rows.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """SELECT * FROM locations where name = %s"""
        items = (self.name,)
        return query, items

    def save(self):
        """
        Generate an insert query to insert a new row in a relation.

        Returns:
            (str, Tuple): A tuple contains the string query and relevant values
        """
        query = """INSERT INTO locations(name) VALUES(%s) RETURNING id;"""
        items = (self.name,)
        return query, items
