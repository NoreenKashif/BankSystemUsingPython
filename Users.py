class User:
    def __init__(self, user_id, name, passwd):
        self.__user_id = user_id
        self.__name = name
        self.__password = passwd

    def print_user(self):
        print("USER_ID: ".ljust(20), self.__user_id)
        print("USER_Name: ".ljust(20), self.__name)
        print("USER_PASSWORD: ".ljust(20), self.__password)

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, n):
        self.__user_id = n

    @property
    def name(self):
        return self.__name

    @name.setter
    def student_marks(self, c):
        self.__name = c





