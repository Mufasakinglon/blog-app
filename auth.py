def authenticate_user(username, password):
    # Implement your authentication logic here
    # For simplicity, we will just use a hardcoded username and password
    if username == 'admin' and password == 'password':
        return True
    return False
