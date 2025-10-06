

from modules.dbconn import DbConn
from modules.expense import Expense
from DB.queries.queries import EXPENSE_QUERIES

class ExpenseRepo:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.user = user
        self.dbname = dbname
        self.password = password
        self.host = host
        self.port = port
    
    def create_expense(self, expense: Expense):
        query = EXPENSE_QUERIES['create_expense']

        params = (expense.user_id, expense.category_id, expense.amount, expense.description)

        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
            
        
    def delete_expense(self, user_id: int, expense_id: int):
        query = EXPENSE_QUERIES['delete_expense']

        params = (user_id, expense_id)

        with DbConn(self.dbname, self.user, self.password, self.host, self.port) as db:
            db.execute(query, params)
        


