

from modules.dbconn import DbConn
from modules.category import Category
from DB.queries.queries import CATEGORY_QUERIES


class CategoryRepo:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.user = user
        self.dbname = dbname
        self.password = password
        self.host = host
        self.port = port
    
    def create_category(self, category: Category) -> int:
        query = CATEGORY_QUERIES['create_category']
        params = (category.name,)

        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
            category_id = db.cur.fetchone()[0]
        return category_id
    
    def delete_category(self, category_id: int):
        query = CATEGORY_QUERIES['delete_categoty']
        params = (category_id,)
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
        
    def get_cat_by_name(self, category_name: str) -> tuple:
        query = CATEGORY_QUERIES['get_cat_by_name']
        params = (category_name,)
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
            category_row = db.cur.fetchone()
        
        return category_row

    def get_cat_by_id(self, category_id: int) -> tuple:
        query = CATEGORY_QUERIES['get_cat_by_id']
        params = (category_id,)
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
            category_row = db.cur.fetchone()
        
        return category_row

    def list_categories(self) -> list[tuple]:
        query = CATEGORY_QUERIES['list_categories']
        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query)
            categoryies_list = db.cur.fetchall()
        
        return categoryies_list
