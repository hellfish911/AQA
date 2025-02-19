import psycopg2
from psycopg2.extras import DictCursor


class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="testdb",
            user="testuser",
            password="testpass",
            host="postgres",
            port="5432"
        )
        self.cur = self.conn.cursor(cursor_factory=DictCursor)

    # Решта методів залишається без змін

    def execute_query(self, query, params=None):
        self.cur.execute(query, params or ())
        self.conn.commit()

    def fetch_data(self, query, params=None):
        self.cur.execute(query, params or ())
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()