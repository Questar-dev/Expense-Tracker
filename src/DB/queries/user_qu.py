

USER_QUERIES = {
    "add_user": "INSERT INTO users(username, full_name, email, password_hash, currency) VALUES (%s, %s, %s, %s, %s);",

    "delete_user":"DELETE FROM users WHERE user_id = %s;",

    "get_user": "SELECT * FROM users WHERE user_id = %s;"
}