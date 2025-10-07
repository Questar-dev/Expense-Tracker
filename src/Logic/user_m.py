

from DB.repositories.user_repo import UserRepo
from modules.user import User

class UserManager:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self._repo = UserRepo(dbname, user, password, host, port)

    def add_user(self, full_name: str, email: str, password: str, currency: str='USA'):
        user = User(full_name, email, password, currency)
        try:
            self._repo.add_user(user)
        except Exception:
            raise Exception("Something is wrong")
    
    def delete_user(self, user_id):
        try:
            self._repo.delete_user(user_id)
        except Exception:
            raise Exception("Something is wrong")
    
    def get_user(self, user_id:int) -> User:
        
        try:
            user_row = self._repo.get_user(user_id)
        except Exception:
            raise Exception("Something is wrong")
        else:
            user = User.factory(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5], user_row[6])

            return user
        
    def authentication(self, entered_email: str, entered_password: str):
        from bcrypt import checkpw
        entered_password = entered_password.encode()
        for user_id, email, hashed_password_str in self._repo.get_users_infos():
            if email == entered_email:
                hashed_password_bytes = hashed_password_str.encode()
                if checkpw(entered_password, hashed_password_bytes):
                    return self.get_user(user_id)
        
        raise Exception("user not found")





