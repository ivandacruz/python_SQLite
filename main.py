import sqlite3
from tkinter import messagebox

class RegistrationSystem:
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
                            image TEXT NOT NULL)''')
    def register_student(self, students):
        self.c.execute("INSERT INTO students(name, email, tel, sex, date_of_birth, address, course, image) VALUES(?,?,?,?,?,?,?,?)",
                    (students))
        self.conn.commit()
        
        messagebox.showinfo('Success', 'registered successfully!')
        
    def view_all_student(self):
        self.c.execute("SELECT * FROM students")
        data = self.c.fetchall()
        
        for i in data:
            print(f'ID: {i[0]} | Name: {i[1]}| e-mail: {i[2]} | Tel: {i[3]} | Sex: {i[4]} | Date of birth: {i[5]} | Address: {i[6]} | Course: {i[7]} | Image: {i[8]}')

    def search_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id))
        data = self.c.fetchone()
        
        print(f'ID: {data[0]} | Name: {data[1]}| e-mail: {data[2]} | Tel: {data[3]} | Sex: {data[4]} | Date of birth: {data[5]} | Address: {data[6]} | Course: {data[7]} | Image: {data[8]}')
        
    def update_student(self, new_values): 
        query = "UPDATE students SET name=?, e-mail=?, tel=?, sex=?, date_of_birth=?, address=?, course=?, image=? WHERE id=?"
        self.c.execute(query, new_values)
        self.conn.commit()
        
        messagebox.showinfo('Success', f'Student with ID:{new_values[8]}  student has been successfully updated!')
        
    
    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()
        
        messagebox.showinfo('Success', f'Student with ID:{id} was deleted successfully!')
        
registration_system = RegistrationSystem()

