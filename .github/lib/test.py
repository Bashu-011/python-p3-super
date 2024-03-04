# class User:
#     def log_in(self):
#         print("User.log_in() called.")
#         self.logged_in = True

# class Student(User):
#     def log_in(self):
#         print("Student.log_in() called.")
#         super().log_in()
#         # self.in_class = True

# oneil = Student()
# oneil.log_in()

# class User:
#     def __init__(self, name):
#         self.name = name

#     def login(self):
#         self.logged_in = True

# class Student(User):
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def login(self):
#         super().login()


class Parent:
    def some_method(self):
        print("Parent's method")

class Child(Parent):
    def some_method(self):
        super().some_method()  # Call the overridden method in the parent class
        print("Child's method")

child_instance = Child()
child_instance.some_method()
