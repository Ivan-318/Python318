import sqlite3
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT* FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_course(self, course_name, price, description):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO courses VALUES(NULL, ?, ?, ?, ?)", (course_name, price, description, tm))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления курса в базу данных" + str(e))
            return False

    def get_course(self, course_id):
        try:
            self.__cur.execute(f"SELECT course_name, price, description FROM courses WHERE id={course_id}")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из базы данных" + str(e))
        return False, False, False

    def get_course_annonce(self):
        try:
            self.__cur.execute("SELECT id, course_name, price, description FROM courses ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курсов из базы данных" + str(e))
        return []
