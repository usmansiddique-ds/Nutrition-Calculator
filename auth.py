import json
import os
import hashlib
from datetime import datetime

USERS_FILE = 'data/users.json'

def init_data():
    """Initialize data folder."""
    os.makedirs('data', exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f)

def hash_password(password):
    """Hash password for security."""
    return hashlib.sha256(
        password.encode()).hexdigest()

def load_users():
    """Load all users from file."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def register_user(username, password, email):
    """Register new user."""
    init_data()
    users = load_users()
    
    if username in users:
        return False, "Username already exists!"
    
    if len(password) < 6:
        return False, "Password must be 6+ chars!"
    
    users[username] = {
        'password': hash_password(password),
        'email': email,
        'created': str(datetime.now()),
        'history': []
    }
    save_users(users)
    return True, "Registration successful!"

def login_user(username, password):
    """Login user."""
    init_data()
    users = load_users()
    
    if username not in users:
        return False, "User not found!"
    
    if users[username]['password'] != \
            hash_password(password):
        return False, "Wrong password!"
    
    return True, "Login successful!"

def save_user_progress(username, data):
    """Save user's nutrition plan."""
    init_data()
    users = load_users()
    
    if username in users:
        users[username]['history'].append({
            'date': str(datetime.now()),
            'data': data
        })
        save_users(users)
        return True
    return False

def get_user_history(username):
    """Get user's past plans."""
    init_data()
    users = load_users()
    
    if username in users:
        return users[username]['history']
    return []