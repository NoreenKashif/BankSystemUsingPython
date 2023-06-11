from Users import User


class Faculty(User):
    def __init__(self, designation, subject):
        self.__designation = designation
        self.__subject = subject

    def print_faculty(self, u):
        print("FACULTY_ID: ".ljust(20), u.user_id)
        print("Name: ".ljust(20), u.name)
        print("DESIGNATION: ".ljust(20), self.__designation)
        print("SUBJECT: ".ljust(20), self.__subject)
        print("-----------------------------------------------------------")

    @property
    def designation(self):
        return self.__designation

    @designation.setter
    def designation(self, d):
        self.__designation = d

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, s):
        self.__subject = s

