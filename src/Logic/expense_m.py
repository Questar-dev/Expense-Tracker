

from DB.repositories.expense_repo import ExpenseRepo
from modules.expense import Expense
from Logic.category_m import CategoryManager




class ExpenseManager:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self._repo = ExpenseRepo(dbname, user, password, host, port)
        self._category_manager = CategoryManager(dbname, user, password, host, port)
    
    def create_expense(self, user_id: int, amount:float, description: str, category_name: str):
        category_id = self.find_category(category_name)
        ex = Expense(user_id, amount, description, category_id)
        try:
            self._repo.create_expense(ex)
        except Exception:
            raise Exception("expense error")

    def delete_expense(self, user_id: int, expense_id: int):
        try:
            self._repo.delete_expense(user_id, expense_id)
        except Exception:
            raise Exception("expense error")
    
    def find_category(self, category_name: str):
        
        category_id = self._category_manager.search_category(category_name, True).category_id

        return category_id


