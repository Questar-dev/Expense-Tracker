

USER_QUERIES = {
    "add_user": "INSERT INTO users(username, full_name, email, password_hash, currency) VALUES (%s, %s, %s, %s, %s) RETURNING user_id, created_at;",

    "delete_user":"DELETE FROM users WHERE user_id = %s;",

    "get_user": "SELECT * FROM users WHERE user_id = %s;",

    "get_users_infos": "SELECT user_id, email, password_hash FROM users;"
}

EXPENSE_QUERIES = {
    "create_expense":"INSERT INTO expenses(user_id, category_id, amount, description) VALUES (%s, %s, %s, %s);",

    "delete_expense": "DELETE FROM expenses WHERE user_id = %s AND expense_id = %s;"
}

CATEGORY_QUERIES = {
    "create_category": "INSERT INTO categories (name) VALUES (%s) RETURNING id;",

    "delete_categoty": "DELETE FROM categories WHERE id = %s;",

    "get_cat_by_name": "SELECT * FROM categories WHERE name = %s;",

    "get_cat_by_id": "SELECT * FROM categories WHERE id = %s;",

    "list_categories": "SELECT * FROM categories;"

}

