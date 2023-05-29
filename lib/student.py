from user import User


class Student(User):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def log_in(self):
        super().log_in()
        self.in_class = True


demi = Student("Demi", "A+")
# demi.log_in()
# print(demi.name, demi.grade)
# print(demi.logged_in)
# print(demi.in_class)
print(demi.__dict__)
