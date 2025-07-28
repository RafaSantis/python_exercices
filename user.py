class User:
    def __init__(self, first, last):
        self.first = first.title()
        self.last = last.title()
        self.login_attempts = 0

    def describe_user(self):
        return f"First name: {self.first}, last name: {self.last}."
    
    def greet_user(self):
        return f"Salutations {self.first} {self.last}."

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
