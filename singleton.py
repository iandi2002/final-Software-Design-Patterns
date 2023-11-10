

class UserAuthenticationSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def authenticate_user(self, username, password):
        valid_users = {"password1": "password1", "2": "2"}

        if username in valid_users and valid_users[username] == password:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Invalid username or password.")
            return False
