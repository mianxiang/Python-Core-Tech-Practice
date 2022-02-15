class DBConnectionManager:
    def __init__(self, hostname, port):
        print('calling __init__')
        self.hostname = hostname
        self.port = port
        self.connection = None
    
    def __enter__(self):
        print('calling __enter__')
        self.connection = DBClient(self.hostname, self.port)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__')
        self.connection.close()

class DBClient:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
    
    def close(self):
        pass


with DBConnectionManager('localhost', '8000') as db_client:
    pass
