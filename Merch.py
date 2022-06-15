import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import Calendar,DateEntry
from insert_db import Db
from Main import Main



class Merch(tk.Toplevel):
    def __init__(self,window,a,app):
        super().__init__()
        self.a=a
        self.db=db
        self.app=app
        self.view=window
        self.open_dialog()

    def open_dialog(self):
        self.title("Merchendaiser")
        self.geometry('250x90')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()
        self.combo = ttk.Combobox(self,width=27,state="readonly")
        self.combo.place(x=1,y=5)
        self.combo.set("Выберите магазин")


        Btn_window1=tk.Button(self,text='Войти', command = self.autarization(self.combo.get()))
        Btn_window1.place(x=1,y=50)
        Btn_window2=tk.Button(self,text='Отмена', command = self.destroy)
        Btn_window2.place(x=100,y=50)

        self.db.cursor.execute('''SELECT address FROM shop''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        self.combo['values']=self.data
        return self.data

    def autarization(self,nameshop):
        self.db.cursor.execute('''SELECT id FROM shop where name = (%s)''',(nameshop))
        self.id_shop=int(self.db.cursor.fetchone()[0])
        Main(self.view,self.app,self.id_shop,self.app)


db=Db()
