from typing import Tuple

import psycopg2
from .config import config
from .constant import CONST


class Connection:
    def __init__(self):
        params = config()
        self.cur = None
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def exec_select(self, query: str, items: Tuple = None):
        self.cur.execute(query, items)
        query_results = self.cur.fetchall()
        return query_results

    def exec_insert(self, query: str, items: Tuple):
        self.cur.execute(query, items)
        item_id = self.cur.fetchone()[0]
        self.conn.commit()
        return int(item_id)

    def process(self, item):
        if item.status == CONST.FAILED:
            return CONST.FAILED
        found = self.exec_select(*item.found())
        if len(found) == 0:
            return self.exec_insert(*item.save())
        return int(found[0][0])

    def close(self):
        self.conn.close()


