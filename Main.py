from Faculty import Faculty
from Users import User
from DB import DBHandler
from Student import Student


def main():
    print("HELLO ! WELCOME TO FCIT")
    print("------------------------------------------------------------------")
    print("PRESS 1 if YOU'RE FROM FACULTY")
    print("\nPRESS 2 if You're a Student")
    print("-------------------------------------------------------------------")
    ch = int(input())
    print("ENTER 1 FOR Register")
    print("Press 2 FOR Login ")
    choice = int(input("Enter your Choice: "))
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    db = DBHandler("localhost", "root", "Vartulo.3", "fcit")
    db.db_connect()
    if ch == 1:
        if choice == 1:
            db.register_faculty()
        if choice == 2:
            print("FOR AUTHENTICATION!!!!!!!")
            db.authenticate_faculty()
            print("YOU HAVE LOG INNED!!!!!!!!!!!")
            print("ENTER 1 if YOU WANT TO VIEW OTHER FACULTY MEMBER's DATA: ")
            print("ENTER 2 if YOU WANT TO VIEW YOUR DATA: ")
            print("ENTER 3 if you WANT TO UPDATE YOUR DATA: ")
            print("ENTER 4 if YOU WANT TO DELETE YOUR DATA: ")
            press = int(input("ENTER YOUR CHOICE: "))
            if press == 1:
                db.view_faculty()
            if press == 2:
                db.get_faculty()
            if press == 3:
                db.update_faculty()
            if press == 4:
                db.delete_faculty()
    if ch == 2:
        if choice == 1:
            db.register_student()
        if choice == 2:
            print("FOR AUTHENTICATION!!!!!!!")
            db.authenticate_student()
            print("you've log in!!!!!!!!")
            print("ENTER 1 if YOU WANT TO VIEW OTHER STUDENT's DATA: ")
            print("ENTER 2 if YOU WANT TO VIEW YOUR DATA: ")
            print("ENTER 3 if you WANT TO UPDATE YOUR DATA: ")
            print("ENTER 4 if YOU WANT TO DELETE YOUR DATA: ")
            press = int(input("ENTER YOUR CHOICE: "))
            if press == 1:
                db.view_students()
            if press == 2:
                print("YOUR DATA: ")
                print("------------------------------------------------------------------------")
                db.get_student()
            if press == 3:
                db.update_student()
            if press == 4:
                db.delete_student()


main()
