import mysql.connector

class DatabaseConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def is_connected(self):
        return self.conn.is_connected()

    def close(self):
        if self.conn.is_connected():
            self.conn.close()
