from insert_db import Db
import tkinter as tk
from tkinter import ttk,messagebox
from Admin import Admin
from Main import Main

class Autarization(tk.Frame):
    def __init__(self,window):
        super().__init__()
        self.db=db
        self.init_login()



    def init_login(self):
        self.label = tk.Label(window, text="Логин ", font=("Arial Bold", 10))
        self.label.place(x=1, y=1)
        self.text1 = ttk.Entry(window,width=30)
        self.text1.place(x=50, y=3)

        self.label2 = tk.Label(window, text="Пароль", font=("Arial Bold", 10))
        self.label2.place(x=1, y=25)
        self.text2 = ttk.Entry(window,show="*",width=30)
        self.text2.place(x=50, y=25)

        Btn_window1=tk.Button(window,text='Войти', command = self.autarization)
        Btn_window1.place(x=120,y=50)
        Btn_window2=tk.Button(window,text='Закрыть', command = window.destroy)
        Btn_window2.place(x=180,y=50)

    def autarization(self):
        try:
            self.login=str(self.text1.get())
            self.password=str(self.text2.get())
            self.db.cursor.execute('''SELECT login From employees where login = (%s) and pass = (%s)''',(self.text1.get(),self.text2.get()))
            self.loginaccept(str(self.db.cursor.fetchone()[0]))
        except:
            messagebox.showinfo('Очень важно', 'Логин или пароль неверный')

    def invize(self):
        self.text1.delete("0","end")
        self.text2.delete("0","end")
        window.withdraw()

    def invizeoff(self):
        window.deiconify()


    def loginaccept(self,login):
        self.db.cursor.execute('''SELECT admin FROM employees where login = (%s)''', (login,))
        if self.db.cursor.fetchone()[0] == True:
            Admin(window,self.db,app)
            self.invize()
        else:
            self.db.cursor.execute('''SELECT id from employees where login = (%s)''',(login,))
            self.id_user=int(self.db.cursor.fetchone()[0])
            Main(window,app,self.id_user)
            self.invize()



db=Db()

window = tk.Tk()
app = Autarization(window)
app.pack()

window.title('Login')
window.geometry('250x90')
window.resizable(False,False)
window.focus_set()
window.mainloop()
