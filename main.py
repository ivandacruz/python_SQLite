import sqlite3
from tkinter import messagebox

class SistemaDeRegistros:
    def __init__(self):
        self.com = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        sefl.c.execute(''' CREATE TABLE IF NOT EXISTS estudants
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome TEXT NOT NULL,
                           email TEXT NOT NULL,
                           telefone TEXT NOT NULL,
                           genero TEXT NOT NULL,
                           data_nascimento TEXT NOT NULL,
                           endereco TEXT NOT NULL,
                           curso TEXT NOT NULL,
                           imagem TEXT NOT NULL''')