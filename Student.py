from Users import User


class Student(User):
    def __init__(self, semester, cgpa, major):
        self.__semester = semester
        self.__student_marks = cgpa
        self.__major = major

    def print_student(self, u):
        print("STUDENT_id: ".ljust(20), u.user_id)
        print("STUDENT_NAME: ".ljust(20), u.name)
        print("SEMESTER: ".ljust(20), self.__semester)
        print("CGPA: ".ljust(20), self.__student_marks)
        print("MAJOR: ".ljust(20), self.__major)
        print("--------------------------------------------")

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, sem):
        self.__semester = sem

    @property
    def student_marks(self):
        return self.__student_marks

    @student_marks.setter
    def student_marks(self, c):
        self.__student_marks = c

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, m):
        self.__major = m
