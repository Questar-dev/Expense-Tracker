

class Expense:
    def __init__(self, user_id: int, amount:float, description: str, category_id: int= None):
        self.expense_id = None
        self.date = None

        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.description = description

    @classmethod
    def factory(cls, expense_id: int, date, user_id: int, amount:float, description: str, category_id: int= None):
        old_expense_obj = cls(user_id, amount, description, category_id)
        old_expense_obj.expense_id = expense_id
        old_expense_obj.date = date
        return old_expense_obj

    


