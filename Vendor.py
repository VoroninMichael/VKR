import tkinter as tk
from tkinter import ttk,messagebox
from insert_db import Db


class Vendor(tk.Toplevel):
    def __init__(self,app):
        super().__init__()
        self.view= app
        self.db=db
        self.addvendor()



    def addvendor(self):
        self.title('добавление нового поставщика')
        self.geometry('325x75')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()

        self.lbl1 = tk.Label(self, text="Имя поставщика", font=("Arial Bold", 10))
        self.lbl1.place(x=1, y=1)
        self.text = ttk.Entry(self,width=30)
        self.text.place(x=125, y=3)

        btn_accept=ttk.Button(self,text="Добавить", command= lambda: self.get_vendor(self.text.get()))

        btn_accept.place(x=150, y=40)

        btn_cancell=ttk.Button(self,text="Закрыть", command=self.destroy)
        btn_cancell.place(x=230, y=40)

    def get_vendor(self,name):
        if self.text.get() == "":
            messagebox.showinfo('Ошибка', 'Введите имя поставщика')
        else:
            self.db.cursor.execute('''SELECT name FROM Vendor''')
            self.data=[]
            k=0
            for row in self.db.cursor.fetchall():
                if row[0] == name:
                    k=k+1
            if k==0:
                self.db.cursor.execute('''INSERT INTO vendor(name) VALUES (%s)''',
                                                (name,))
                self.db.connection.commit()
                messagebox.showinfo('Очень важно', 'Поставщик добавлен')
                self.text=""


            else:
                messagebox.showinfo('Ошибка', 'Такой поставщик уже есть')
            return k


db=Db()
