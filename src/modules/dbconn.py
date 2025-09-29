


class DbConn:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.user = user
        self.dbname = dbname
        self.password = password
        self.host = host
        self.port = port

        self.conn = None
        self.cur = None
    
    def __enter__(self):
        import psycopg2
        self.conn = psycopg2.connect(
            dbname = self.dbname,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
        )
        self.cur = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
    
    def execute(self, query: str, params: tuple=()):
        self.cur.execute(query, params)


