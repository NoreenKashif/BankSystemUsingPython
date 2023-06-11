from Student import Student
from Faculty import Faculty
from Users import User
from Exceptions import *


def input_user():
    user_name = input("Enter Your User Name: ")
    password = input("Enter your PASSWORD: ")
    try:
        if len(password) != 4:
            raise InvalidPassword("Pin should be 4 digits!!!!!!!!")
    except InvalidPassword as ie:
        print(ie)
        while len(password) != 4:
            password = input("Enter Valid  4-digit PASSWORD: ")
    user_data = (user_name, password)
    return user_data


def input_user_for_registration():
    user_name = input("Enter User Name: ")
    password = input("Enter a 4- digit PASSWORD: ")
    try:
        if len(password) != 4:
            raise InvalidPassword("Pin should be 4 digits!!!!!!!!")
    except InvalidPassword as ie:
        print(ie)
        while len(password) != 4:
            password = input("Enter Valid  4-digit PASSWORD: ")
    re_enter_password = input("Confirm PASSWORD: ")
    if re_enter_password == password:
        user_tuple = (user_name, password)
        return user_tuple
    else:
        try:
            if re_enter_password != password:
                raise PasswordNotMatch("PASSWORD NOT MATCH")
        except PasswordNotMatch as ie:
            print(ie)
            while re_enter_password != password:
                password = input("Enter Password Again: ")
                re_enter_password = input("Confirm Password")
            user_tuple = (user_name, password)
            return user_tuple


def input_student_data():
    sem = input("Enter your current Semester: ")
    marks = input("Enter your CGPA: ")
    major = input("Enter Your MAJOR: ")
    stu_tuple = (sem, marks, major)
    return stu_tuple


def input_faculty():
    designation = input("Enter your DESIGNATION: ")
    subject = input("Enter your SUBJECT: ")
    fac_tuple = (designation, subject)
    return fac_tuple


def input_semester_for_update_student():
    sem = int(input("Enter semester you want to update"))
    return sem


def input_cgpa_for_update_student():
    c = float(input("Enter CGPA you want to update"))
    return c


def input_major_for_update_student():
    m = input("Enter MAJOR you want to update")
    return m


def input_func_to_select_which_attribute_to_update():
    update_data = input("Which data you want to update")
    return update_data


def input_designation_for_update_faculty():
    d = input("Enter DESIGNATION you want to update: ")
    return d


def input_subject_for_update_faculty():
    s = input("ENTER SUBJECT you want to update: ")
    return s


def msg_for_password_confirmation():
    print("PASSWORD RESET SUCCESSFULLY!!!!!!")


def msg_for_wrong_password():
    print("FORGOT Password?")
    en = int(input("Enter 1 if you Forgot password: "))
    return en


def msg_for_user_to_ask_registration():
    print("REGISTER USER FIRST:!!!!!!")

