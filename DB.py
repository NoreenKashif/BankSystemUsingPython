import pymysql
from Users import User
from Student import Student
from Utils import *
from Faculty import Faculty


class DBHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.passwd = password
        self.database = database
        self.cursor = None
        self.con = None

    def db_connect(self):
        try:
            self.con = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)
            self.cursor = self.con.cursor()
        except Exception as e:
            print(str(e))

    def db_disconnect(self):
        if self.con != None:
            self.con.close()
        if self.cursor != None:
            self.cursor.close()

    def register_student(self):
        user = input_user_for_registration()
        args = (user[0], user[1])
        sql_query ="INSERT INTO fcit.user (usernamel, password) VALUES (%s, %s)";
        self.cursor.execute(sql_query, args)
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s AND password = %s;"
        self.cursor.execute(sql_q, args)
        user_id = self.cursor.fetchall()
        sql_q1 = "INSERT INTO `fcit`.`student` (`semester`, `cgpa`, `major`, `user_id`) VALUES (%s, %s, %s , %s);"
        stu = input_student_data()
        args1 = (stu[0], stu[1], stu[2], user_id[0])
        self.cursor.execute(sql_q1, args1)
        self.con.commit()

    def register_faculty(self):
        user1 = input_user_for_registration()
        arg = (user1[0], user1[1])
        sql_query1 = "INSERT INTO fcit.user (usernamel, password) VALUES (%s, %s)";
        self.cursor.execute(sql_query1, arg)
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s AND password = %s;"
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        sql_q1 = "INSERT INTO `fcit`.`faculty` (`designation`, `subject`, `user_id`) VALUES (%s, %s, %s );"
        fac = input_faculty()
        args1 = (fac[0], fac[1], user_id[0])
        self.cursor.execute(sql_q1, args1)
        self.con.commit()

    def view_students(self):
        user = input_user()
        sql_query = "Select student.user_id, user.usernamel, user.password, student.semester, student.cgpa, student.major FROM fcit.user JOIN fcit.student ON fcit.student.user_id = user.id;"
        self.cursor.execute(sql_query)
        results = self.cursor.fetchall()
        for r in results:
            u = User(r[0], r[1], r[2])
            stu = Student(r[3], r[4], r[5])
            stu.print_student(u)

    def view_faculty(self):
        sql_query = "Select user.id, user.usernamel,user.password, faculty.designation, faculty.subject FROM fcit.user JOIN fcit.faculty ON fcit.faculty.user_id = user.id;"
        self.cursor.execute(sql_query)
        results = self.cursor.fetchall()
        for r in results:
            u = User(r[0], r[1], r[2])
            fac = Faculty(r[3], r[4])
            fac.print_faculty(u)

    def get_faculty(self):
        user = input_user()
        sql_query = "SELECT fcit.user.id, fcit.user.usernamel, fcit.user.password, fcit.faculty.designation, fcit.faculty.subject FROM fcit.user JOIN fcit.faculty ON faculty.user_id = user.id WHERE user.usernamel = %s  AND user.password = %s ;"
        args = (user[0], user[1])
        self.cursor.execute(sql_query, args)
        results = self.cursor.fetchall()
        for i in results:
            u = User(i[0], i[1], i[2])
            faculty = Faculty(i[3], i[4])
            faculty.print_faculty(u)

    def get_student(self):
        user = input_user()
        arg = (user[0], user[1])
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s AND password = %s;"
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        #print(len(user_id))
        sql_query = "SELECT user.id, student.semester, student.cgpa, student.major FROM fcit.student JOIN fcit.user ON student.user_id = user.id WHERE (student.user_id =%s)  AND (user.password = %s) ;"
        args = (user_id[0][0], user[1])
        self.cursor.execute(sql_query, args)
        results = self.cursor.fetchall()
        u = User(user_id[0][0], user[0], user[1])
        #u.print_user()
        for r in results:
            stu = Student(r[1], r[2], r[3])
            stu.print_student(u)

    def update_user(self):
        u = input_user_for_registration()
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s;"
        self.cursor.execute(sql_q, (u[0],))
        user_id = self.cursor.fetchall()
        sql_query = "UPDATE fcit.user u SET u.password = %s WHERE (u.id =%s) ;"
        self.cursor.execute(sql_query, (u[1],user_id[0][0]))
        self.con.commit()

    def update_faculty(self):
        u = input_user()
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s AND password = %s;"
        arg = (u[0], u[1])
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        data_to_be_updated = input_func_to_select_which_attribute_to_update()
        data_to_be_updated = data_to_be_updated.lower()
        if data_to_be_updated == "designation":
            des = input_designation_for_update_faculty()
            sql_query = "UPDATE fcit.faculty f SET f.designation = %s WHERE (f.user_id =%s) ;"
            args = (des, user_id[0])
            self.cursor.execute(sql_query, args)
            results = self.cursor.fetchall()
            self.con.commit()
        if data_to_be_updated == "subject":
            sub = input("Enter the value to be updated: ")
            sql_query = "UPDATE fcit.faculty f SET f.subject = %s WHERE (f.user_id =%s) ;"
            args = (sub, user_id[0])
            self.cursor.execute(sql_query, args)
            results1 = self.cursor.fetchall()
            self.con.commit()

    def update_student(self):
        u = input_user()
        data_to_be_updated = input_func_to_select_which_attribute_to_update()
        data_to_be_updated = data_to_be_updated.lower()
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s AND password = %s;"
        arg = (u[0], u[1])
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        if data_to_be_updated == "semester":
            sem = input_semester_for_update_student()
            sql_query = "UPDATE fcit.student s SET s.semester = %s WHERE (s.user_id =%s) ;"
            args = (sem, user_id[0])
            self.cursor.execute(sql_query, args)
            results = self.cursor.fetchall()
            self.con.commit()
        if data_to_be_updated == "cgpa":
            c = input_cgpa_for_update_student()
            sql_query = "UPDATE fcit.student s SET s.cgpa = %s WHERE (s.user_id =%s) ;"
            args = (c, user_id[0])
            self.cursor.execute(sql_query, args)
            results = self.cursor.fetchall()
            self.con.commit()
        if data_to_be_updated == "major":
            m = input_major_for_update_student()
            sql_query = "UPDATE fcit.student s SET s.major = %s WHERE (s.user_id =%s) ;"
            args = (m, user_id[0])
            self.cursor.execute(sql_query, args)
            results = self.cursor.fetchall()
            self.con.commit()

    def authenticate_student(self):
        u = input_user()
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s ;"
        arg = (u[0],)
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        us = user_id[0][0]
        sql_query = "SELECT EXISTS(SELECT * from fcit.student WHERE student.user_id = %s );"
        self.cursor.execute(sql_query, (us,))
        result = self.cursor.fetchall()
        # print("RESULT!!!!!!!!!!!", result)
        if result[0][0] == 1:
            sql_query1 = "SELECT EXISTS(SELECT * from fcit.user WHERE user.password = %s);"
            self.cursor.execute(sql_query1, (u[1],))
            result1 = self.cursor.fetchall()
            if result1[0][0] == 0:
                try:
                    raise WrongPassword("WRONG PASSWORD")
                except WrongPassword as e:
                    print(e)
                    en = msg_for_wrong_password()
                    if en == 1:
                        self.update_user()
                        msg_for_password_confirmation()
        if result[0][0] == 0:
            try:
                raise UserNotFound("USER NOT FOUND")
            except UserNotFound as w:
                print(str(w))
                msg_for_user_to_ask_registration()
                self.register_student()

    def authenticate_faculty(self):
        u = input_user()
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s ;"
        arg = (u[0],)
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        us = user_id[0][0]
        #print(us)
        sql_query = "SELECT EXISTS(SELECT * from fcit.faculty WHERE faculty.user_id = %s );"
        self.cursor.execute(sql_query, (us, ))
        result = self.cursor.fetchall()
        # print("RESULT!!!!!!!!!!!", result)
        if result[0][0] == 1:
            sql_query1 = "SELECT EXISTS(SELECT * from fcit.user WHERE user.password = %s);"
            self.cursor.execute(sql_query1, (u[1],))
            result1 = self.cursor.fetchall()
            try:
                if result1[0][0] != 1:
                    raise WrongPassword("WRONG PASSWORD")
            except WrongPassword as e:
                print(e)
                en = msg_for_wrong_password()
                if en == 1:
                    self.update_user()
                    msg_for_password_confirmation()
        if result[0][0] == 0:
            try:
                raise UserNotFound("USER NOT FOUND")
            except UserNotFound as w:
                print(str(w))
                msg_for_user_to_ask_registration()
                self.register_faculty()

    def delete_student(self):
        u = input_user()
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s AND password = %s;"
        arg = (u[0], u[1])
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        us = user_id[0][0]
        sql_query = "DELETE FROM fcit.student WHERE student.user_id = %s;"
        self.cursor.execute(sql_query, (us, ))
        sql_q1 = "DELETE FROM fcit.user WHERE user.id = %s AND user.usernamel = %s ;"
        self.cursor.execute(sql_q1, (us, u[0]))
        self.con.commit()

    def delete_faculty(self):
        u = input_user()
        sql_q = "SELECT user.id FROM fcit.user WHERE usernamel = %s AND password = %s;"
        arg = (u[0], u[1])
        # print(u)
        self.cursor.execute(sql_q, arg)
        user_id = self.cursor.fetchall()
        us = user_id[0][0]
        # print(us)
        sql_query = "DELETE FROM fcit.faculty WHERE faculty.user_id = %s ;"
        self.cursor.execute(sql_query, (us,))
        sql_q1 = "DELETE FROM fcit.user WHERE user.id = %s AND user.usernamel = %s ;"
        self.cursor.execute(sql_q1, (us, u[0]))
        self.con.commit()


