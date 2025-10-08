

from DB.repositories.category_repo import CategoryRepo
from modules.category import Category

class CategoryManager:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self._repo = CategoryRepo(dbname, user, password, host, port)
    
    def create_category(self, category_name: str) -> Category:
        cat = Category(category_name)
        try:
            category_id = self._repo.create_category(cat)
        except Exception:
            raise Exception("category error")
        else:
            cat.category_id = category_id
            return cat
    
    def search_category(self, category_name: str, create_ifno: bool= False) -> Category:
        """it searches a category for the given category name, if nothing found, it creates one."""
        try:
            category_row = self._repo.get_cat_by_name(category_name)
        except Exception:
            raise Exception("category error")
        
        else:
            if category_row:
                cate = Category.factory(category_row[0], category_row[1])
                return cate
            else:
                if create_ifno:
                    cate = self.create_category(category_name)
                    return cate

    def delete_category(self, category_id: int):
        category = self.get_cat_by_id(category_id)
        if not category:
            raise Exception("category not found")
        try:
            self._repo.delete_category(category_id)
        except Exception:
            raise Exception('category error')

    def get_cat_by_id(self, category_id: int) -> Category:
        try:
            category_row = self._repo.get_cat_by_id(category_id)
        except Exception:
            raise Exception('category error')
        else:
            cate = Category.factory(category_row[0], category_row[1])
            return cate

    def list_categories(self) -> list[Category]:
        try:
            categories_list = self._repo.list_categories()
        except Exception:
            raise Exception('category error')
        else:
            categories = []
            for category_row in categories_list:
                cate = Category.factory(category_row[0], category_row[1])
                categories.append(cate)
            return categories
