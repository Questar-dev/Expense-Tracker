


from modules.dbconn import DbConn
from modules.user import User
from DB.queries.queries import USER_QUERIES

class UserRepo:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.user = user
        self.dbname = dbname
        self.password = password
        self.host = host
        self.port = port

    def add_user(self, user: User):
        query = USER_QUERIES['add_user']

        params = (user.username, user.full_name, user.email, user.password_hash, user.currency)
        
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
    
    def delete_user(self, user_id):
        query = USER_QUERIES['delete_user']
        params = (user_id,)
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
    
    def get_user(self, user_id)-> tuple:
        query = USER_QUERIES['get_user']
        params = (user_id,)
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
            user_row = db.cur.fetchone()
        
        return user_row
    
    def get_users_infos(self) -> list[tuple]:
        """Returns a list of (user_id, email, password)"""
        query = USER_QUERIES['get_users_infos']
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query)
            users_list = db.cur.fetchall()
        
        return users_list


