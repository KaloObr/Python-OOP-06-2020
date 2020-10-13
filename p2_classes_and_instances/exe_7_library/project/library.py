from collections import defaultdict
# from PythonOOP.p2_classes_and_instances.exe_7_library.project.users import User
# from PythonOOP.Classes_and_Instances_2.exe_7_library.project.users import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # dict regarding authors (keys) and books avaiable for each (list)
        self.rented_books = defaultdict({})

    def add_user(self, user: User):
        if user in self.user_records:
            return f"User with id = {user} already registered in the library!"
        self.user_records.append(user)

    def rempve_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def check_user_id(self, user_id):
        list_of_user_ids = []
        for user in self.user_records:
            if user_id == user.user_id:
                list_of_user_ids.append(user_id)

    def change_username(self, user_id: int, new_username: str):
        list_of_ids = [user for user in self.user_records if user_id == user.user_id]

        if user_id not in list_of_ids:
            return f"There is no user with id = {user_id}!"
        else:
            pass



person = User(15, "kalo")
lib = Library()

print(lib.add_user(person))


















