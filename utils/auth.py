# /utils/auth.py

# This is a placeholder logic for login/signup using phone number.
# You can later replace it with real database logic.

users_db = {}

def signup_user(name, phone):
    if phone in users_db:
        return False, "User already exists"
    users_db[phone] = {"name": name}
    return True, "Signup successful"

def login_user(phone):
    if phone in users_db:
        return True, "Login successful", users_db[phone]
    return False, "User not found", None
