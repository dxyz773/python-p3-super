class User:
    def __init__(self, name):
        self.name = name

    def log_in(self):
        self.logged_in = True


admin = User("Sarah")
admin.log_in()

# print(admin.logged_in, admin.name)
