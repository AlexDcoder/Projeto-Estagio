from typing import Optional


class Connector:
    def __init__(
        self, host: str, port: int, database: str, user: str,
        password: Optional[str] = None,
    ):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def is_connected(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute_query(self, query):
        pass

    def import_to_csv(self):
        pass
