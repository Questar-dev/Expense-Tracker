

import bcrypt
class User:
    def __init__(self, full_name: str, email: str, password: str, currency: str='USA'):

        self.user_id = None # Genearetd in the DB

        self.full_name = full_name
        self.username = self.gen_username(full_name)
        self.email = email
        self.password_hash = self.hash_password(password)
        self.currency = currency

        self.created_at = None # Genearetd in the DB

    def hash_password(self, password: str) -> str:
        password_in_bytes = password.encode()

        hashed_password_in_str = bcrypt.hashpw(password_in_bytes, bcrypt.gensalt()).decode()

        return hashed_password_in_str
    
    def gen_username(self, full_name):
        return full_name + '#01'

    @classmethod
    def factory(cls, user_id, username, full_name: str, email: str, password: str, currency: str, created_at):
        old_user_obj = cls(full_name, email, password, currency)
        old_user_obj.user_id = user_id
        old_user_obj.username = username
        old_user_obj.created_at = created_at

        return old_user_obj

    

