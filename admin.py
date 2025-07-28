import user

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges

class Admin(user.User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = Privileges()  # começa com vazio
