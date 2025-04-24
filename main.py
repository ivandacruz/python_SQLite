import sqlite3
from tkinter import messagebox

class SistemaDeRegistros:
    def __init__(self):
        self.com = sqlite3.connect('student.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            e-mail TEXT NOT NULL,
                            tel TEXT NOT NULL,
                            sex TEXT NOT NULL,
                            date_of_birth TEXT NOT NULL,
                            address TEXT NOT NULL,
                            course TEXT NOT NULL,
                            picture TEXT NOT NULL)''')
    def register_student(self, students):
        self.c.execute("INSERT INTO students(name, email, tel, sex, date_of_birth, address, course, picture) VALUES(?,?,?,?,?,?,?,?)",
                    (students))
