class Connector:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute_query(self, query):
        pass
