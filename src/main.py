
from time import sleep

# Looger
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.FileHandler('app.log', 'w')
frmtr = logging.Formatter('%(asctime)s | %(name)s | %(message)s')
handler.setFormatter(frmtr)
log.addHandler(handler)


# ------------
from Logic.user_m import UserManager, User
from Logic.expense_m import ExpenseManager
from Logic.category_m import CategoryManager

from os import getenv, system as sys
from dotenv import load_dotenv

load_dotenv()
db_name = getenv('DB_NAME')
db_user = getenv('USER')
db_password = getenv('PASSWORD')
db_host = getenv('HOST')
db_port = getenv('PORT')



def auth_menue() -> int:
    return int(input("""
1. Login
2. Sign in
3. Exit
""").strip())

def app_menue() -> int:
    while True:
        try:
            option = int(input("""
    1. View Expenses (another options) (Soon)
    2. Add Expense
    3. Delete Expense (Soon)
    4. View Categories
    5. Add Category (Soon)
    6. Log out
    """).strip())
            if option > 6 or option <= 0:
                raise ValueError            
            return option
        except ValueError:
            print('Enter a number between 1 and 5.')

def app():
    
    current_user = None
    um = UserManager(db_name, db_user, db_password, db_host, db_port)
    em = ExpenseManager(db_name, db_user, db_password, db_host, db_port)
    cm = CategoryManager(db_name, db_user, db_password, db_host, db_port)


    while True:

        if current_user is None:
            option = auth_menue()
            match option: # Auth
                case 1: # Login
                    sys('cls')
                    email = input('Email: ').strip()
                    password = input('password: ').strip()
                    try:
                        current_user = um.authentication(email, password)
                    except Exception as e :
                        log.error(e)
                    else:
                        print(f"Wolcome back '{current_user.username}'")
                        sleep(2)

                case 2: # Sign in
                    sys('cls')
                    full_name = input('Full Name: ').strip()
                    email = input('Email: ').strip()
                    password = input('Password: ').strip()
                    currency = input('Currency: ').strip()
                    try:
                        current_user = um.add_user(full_name, email, password, currency or 'USA')
                    except Exception as e:
                        log.error(e)
                    else:
                        print(f"Thenks for joining the family {current_user.username}")
                        sleep(2)
   
                case 3: # Exit
                    print("Exiting")
                    break
        
        if isinstance(current_user, User):
            sys('cls')
            option = app_menue()
            match option:
                case 1: # view expenses
                    pass                
                case 2: # add expense
                    sys('cls')
                    amount = float(input('Amount: ').strip())
                    description = input('Description: ').strip()
                    category_name = input('Category Name: ').strip()
                    try:
                        em.create_expense(current_user.user_id, amount, description, category_name)
                    except Exception as e :
                        log.error(e)
                    else:
                        print('Expense added successfully.')
                case 3: # delete expense
                    pass
                case 4: # view categories
                    try:
                        categories = cm.list_categories()
                        log.debug(f'{categories}')
                    except Exception as e :
                        log.error(e)
                    else:
                        if categories:
                            for cate in categories:
                                print(cate)
                                print('-'*10)
                            sleep(5)
                        else:
                            print("No Categories")
                            sleep(2)
                case 5: # Add Category
                    pass
                case 6: # logout
                    current_user = None


if __name__ == "__main__":
    app()




            






