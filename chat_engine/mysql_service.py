import pandas as pd

class MySQLService:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def execute_query(self, query):
        self.cursor = self.connection.conn.cursor()
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_column_names(self):
        return [desc[0] for desc in self.cursor.description]

    def create_dataframe(self, results):
        column_names = self.get_column_names()
        return pd.DataFrame(results, columns=column_names)
