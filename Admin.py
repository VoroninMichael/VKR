import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import Calendar,DateEntry
from insert_db import Db
from Main import Main




class Admin (tk.Toplevel):
    def __init__(self,window,db,app):
        super().__init__(window)
        self.window=window
        self.db=db
        self.app=app
        self.dialog_on()


    def dialog_on(self):
        self.title("Admin")
        self.geometry('580x300')
        self.resizable(False,False)


        self.combo = ttk.Combobox(self,width=27,state="readonly")
        self.combo['values']=combo
        self.combo.place(x=150,y=5)
        self.combo.set("Выберите объект")
        self.combo.bind("<<ComboboxSelected>>",self.lll)
        btn_shop=ttk.Button(self,text="Добавить магазин",width=20,command=self.createshop)
        btn_shop.place(x=1, y=10)

        btn_employe=ttk.Button(self,text="Добавить сотрудника",width=20,command=self.createmploye)
        btn_employe.place(x=1, y=40)

        btn_employe=ttk.Button(self,text="Добавить вид обуви",width=20,command=self.creattype)
        btn_employe.place(x=1, y=70)

        btm_showcase=ttk.Button(self,text="Создать витрину",width=20,command=self.creatshowcase)
        btm_showcase.place(x=1, y=100)
        btm_subdepartament=ttk.Button(self,text="Создать подотдел",width=20,command=self.creatsubdepartament)
        btm_subdepartament.place(x=1, y=130)

        btm_departament=ttk.Button(self,text="Создать отдел",width=20,command=self.creatdepartament)
        btm_departament.place(x=1, y=160)

        btm_merch=ttk.Button(self,text="Окно мерчендайзера",width=20,command=self.merch)
        btm_merch.place(x=1, y=190)


        Btn_close=tk.Button(self,text='Выход', command=self.out)
        Btn_close.place(x=3,y=260)


        self.tree= ttk.Treeview(self,columns=('a','b'),height=10,  show='headings')

        self.tree.column('a', width=20, anchor=tk.CENTER)
        self.tree.column('b', width=380, anchor=tk.CENTER)

        self.tree.heading('a',text=' ')
        self.tree.heading('b',text=' ')
        self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
        self.tree.configure(yscroll=self.ysb.set)
        self.ysb.pack(side=tk.RIGHT,fill="y")
        self.tree.place(x=150,y=30)

        btm_merch=ttk.Button(self,text="Изменить",width=20)
        btm_merch.place(x=150, y=260)
        btm_merch=ttk.Button(self,text="Удалить",width=20)
        btm_merch.place(x=290, y=260)


    def merch(self):
        self.destroy()
        self.a=Admin(self.window,self.db,self.app)
        Merch(self.window,self.a,self.app,self.db)


    def lll(self,select):
        if self.combo.get() == "Магазин":
            self.tree.destroy()
            self.ysb.destroy()
            self.tree= ttk.Treeview(self,columns=('a','b'),height=10,  show='headings')

            self.tree.column('a', width=250, anchor=tk.CENTER)
            self.tree.column('b', width=150, anchor=tk.CENTER)

            self.tree.heading('a',text='Адрес')
            self.tree.heading('b',text='Вместительность')

            self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
            self.tree.configure(yscroll=self.ysb.set)
            self.ysb.pack(side=tk.RIGHT,fill="y")
            self.tree.place(x=150,y=30)
            self.view_shop()

        if self.combo.get() == "Сотрудники":
            self.tree.destroy()
            self.ysb.destroy()
            self.tree= ttk.Treeview(self,columns=('a','b','c'),height=10,  show='headings')

            self.tree.column('a', width=134, anchor=tk.CENTER)
            self.tree.column('b', width=133, anchor=tk.CENTER)
            self.tree.column('c', width=133, anchor=tk.CENTER)
            self.tree.heading('a',text='Магазин')
            self.tree.heading('b',text='Имя')
            self.tree.heading('c',text='Логин')
            self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
            self.tree.configure(yscroll=self.ysb.set)
            self.ysb.pack(side=tk.RIGHT,fill="y")
            self.tree.place(x=150,y=30)
            self.view_employee()
        if self.combo.get() == "Виды":
            self.tree.destroy()
            self.ysb.destroy()
            self.tree= ttk.Treeview(self,columns=('a','b','c'),height=10,  show='headings')

            self.tree.column('a', width=134, anchor=tk.CENTER)
            self.tree.column('b', width=133, anchor=tk.CENTER)
            self.tree.column('c', width=133, anchor=tk.CENTER)
            self.tree.heading('a',text='Вид')
            self.tree.heading('b',text='Подвид')
            self.tree.heading('c',text='Пол')
            self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
            self.tree.configure(yscroll=self.ysb.set)
            self.ysb.pack(side=tk.RIGHT,fill="y")
            self.tree.place(x=150,y=30)
            self.view_type()
        if self.combo.get() == "Витрины":
            self.tree.destroy()
            self.ysb.destroy()
            self.tree= ttk.Treeview(self,columns=('a','b','c'),height=10,  show='headings')

            self.tree.column('a', width=200, anchor=tk.CENTER)
            self.tree.column('b', width=75, anchor=tk.CENTER)
            self.tree.column('c', width=125, anchor=tk.CENTER)

            self.tree.heading('a',text='Витрина')
            self.tree.heading('b',text='Высота')
            self.tree.heading('c',text='Вместительность')
            self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
            self.tree.configure(yscroll=self.ysb.set)
            self.ysb.pack(side=tk.RIGHT,fill="y")
            self.tree.place(x=150,y=30)
            self.view_showcase()
        if self.combo.get() == "Подотделы":
            self.tree.destroy()
            self.ysb.destroy()
            self.tree= ttk.Treeview(self,columns=('a','b'),height=10,  show='headings')

            self.tree.column('a', width=200, anchor=tk.CENTER)
            self.tree.column('b', width=200, anchor=tk.CENTER)

            self.tree.heading('a',text='Подотдел')
            self.tree.heading('b',text='Витрина')

            self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
            self.tree.configure(yscroll=self.ysb.set)
            self.ysb.pack(side=tk.RIGHT,fill="y")
            self.tree.place(x=150,y=30)
            self.view_subdept()


        if self.combo.get() == "Отделы":
            self.tree.destroy()
            self.ysb.destroy()
            self.tree= ttk.Treeview(self,columns=('a','b','c'),height=10,  show='headings')

            self.tree.column('a', width=134, anchor=tk.CENTER)
            self.tree.column('b', width=133, anchor=tk.CENTER)
            self.tree.column('c', width=133, anchor=tk.CENTER)
            self.tree.heading('a',text='Магазин')
            self.tree.heading('b',text='Отдел')
            self.tree.heading('c',text='Подотдел')
            self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
            self.tree.configure(yscroll=self.ysb.set)
            self.ysb.pack(side=tk.RIGHT,fill="y")
            self.tree.place(x=150,y=30)
            self.view_dept()




    def view_shop(self):
        self.db.cursor.execute('''select address,countmax from shop''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]
    def view_employee(self):
        self.db.cursor.execute('''select shop.address, employees.name,employees.login from shop
        inner join employees on employees.id_shop = shop.id''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]
    def view_type(self):
        self.db.cursor.execute('''select dept.name, subdept.name,dept_subdept.sex from dept
        inner join dept_subdept on dept.id = dept_subdept.id_dept
        inner join subdept on subdept.id = dept_subdept.id_subdept''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]

    def view_showcase(self):
        [self.tree.delete(i) for i in self.tree.get_children()]
        self.db.cursor.execute('''select id from showcase''')
        for row in self.db.cursor.fetchall():
            self.db.cursor.execute('''select sum(shelf.kappa) from shelf
                                      inner join showcase_shelf on shelf.id = showcase_shelf.id_shelf
                                      inner join showcase on showcase.id = showcase_shelf.id_showcase
                                      where showcase.id = (%s)''',(row[0],))
            self.sumkappa=self.db.cursor.fetchone()[0]
            self.db.cursor.execute('''select levelmax from showcase where id= (%s)''',(row[0],))
            self.levelmax=self.db.cursor.fetchone()[0]
            self.db.cursor.execute('''select name from showcase where id= (%s)''',(row[0],))
            self.showcasename=self.db.cursor.fetchone()[0]
            self.tree.insert('', 'end', values=(self.showcasename,self.levelmax,self.sumkappa))

    def view_subdept(self):
        self.db.cursor.execute('''select depttype.name, subdept_showcase.name from depttype
        inner join subdept_showcase on subdept_showcase.id = depttype.id_subdept''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]


    def view_dept(self):
        self.db.cursor.execute('''select shop.address, departament.name,depttype.name from shop
        inner join departament on departament.id_shop = shop.id
        inner join depttype on departament.id_depttype = depttype.id''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]




    def createshop (self):
        Konstructshop(self.db)
    def createmploye (self):
        Konstructemploye(self.db)
    def creattype(self):
        Konstructtype(self.db)
    def creatshowcase(self):
        Konstructshowcase(self.db)
    def creatsubdepartament(self):
        Konstructsubdeparament(self.db)

    def creatdepartament(self):
        Konstructdeparament(self.db)

    def out(self):
        self.app.invizeoff()
        self.destroy()

class Konstructshop(tk.Toplevel):
    def __init__(self,db):
        self.db=db
        super().__init__()
        self.dialog_on()


    def dialog_on(self):
        self.title("Create shop")
        self.geometry('350x100')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()

        self.lbl1 = tk.Label(self, text="Адрес магазина", font=("Arial Bold", 10))
        self.lbl1.place(x=1, y=1)
        self.text = ttk.Entry(self,width=30)
        self.text.place(x=125, y=3)
        self.lbl2 = tk.Label(self, text="Ограничения на складе", font=("Arial Bold", 10))
        self.lbl2.place(x=1, y=30)
        self.spin1 = tk.Spinbox(self,from_=1,to=1000000, width=5)
        self.spin1.place(x=150,y=30)

        btn_ok=ttk.Button(self,text="Добавить",command= lambda: self.record_shop (self.text.get(),self.spin1.get()))
        btn_ok.place(x=235, y=60)



    def record_shop (self,address,countmax):
        if self.text.get() == "":
            messagebox.showinfo('Ошибка', 'Введите имя магазина')
        else:
            self.db.cursor.execute('''SELECT address FROM shop''')
            self.data=[]
            k=0
            for row in self.db.cursor.fetchall():
                if row[0] == address:
                    k=k+1
            if k==0:
                self.db.insert_shop(address,countmax)
                messagebox.showinfo('Очень важно', 'Магазин добавлен')
                self.destroy()
            else:
                messagebox.showinfo('Ошибка', 'Такой магазин уже есть')
        return k

class Konstructemploye(tk.Toplevel):
    def __init__(self,db):
        self.db=db
        super().__init__()

        self.dialog_on()

    def dialog_on(self):
        self.title("Create employees")
        self.geometry('375x175')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()

        self.lbl1 = tk.Label(self, text="Имя фамилия сотрудника", font=("Arial Bold", 10))
        self.lbl1.place(x=1, y=1)
        self.text1 = ttk.Entry(self,width=30)
        self.text1.place(x=175, y=3)

        self.lbl2 = tk.Label(self, text="Логин", font=("Arial Bold", 10))
        self.lbl2.place(x=1, y=30)
        self.text2 = ttk.Entry(self,width=30)
        self.text2.place(x=175, y=30)

        self.lbl3 = tk.Label(self, text="Пароль", font=("Arial Bold", 10))
        self.lbl3.place(x=1, y=60)
        self.text3 = tk.Entry(self,width=30)
        self.text3.place(x=175, y=60)

        self.status=tk.IntVar()
        self.status.set(0)
        self.chek = tk.Checkbutton(self, text='Администратор',variable= self.status, onvalue=1, offvalue=0)
        self.chek.place(x=1, y=90)





        self.lbl4 = tk.Label(self, text="Магазин", font=("Arial Bold", 10))
        self.lbl4.place(x=1, y=120)
        self.combo1 = ttk.Combobox(self,width=27,state="readonly")
        self.combo1['values']=self.view_adress()
        self.combo1.place(x=175,y=120)

        btn_ok=ttk.Button(self,text="Добавить", command = lambda : self.records_employee(self.text1.get(),
                                                                                      self.text2.get(),
                                                                                       self.text3.get(),
                                                                                       self.status.get(),
                                                                                       self.combo1.get()))
        btn_ok.place(x=290, y=150)


    def view_adress(self):
        self.db.cursor.execute('''SELECT address FROM shop''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        return self.data


    def records_employee(self,name,login,password,admin,address):
        try:
            self.db.cursor.execute('''SELECT login FROM employees''')
            self.data=[]
            k=0
            for row in self.db.cursor.fetchall():
                if row[0] == login:
                    k=k+1
            if k==0:
                self.db.insert_employe(name,login,password,admin,address)
                self.clear()
                messagebox.showinfo('Очень важно', 'Выполнено')
            else:
                messagebox.showinfo('Ошибка', 'Этот логин занят')

        except:
            messagebox.showinfo('Ошибка', 'Не все данные занесены или занесены не коректно')
        return k


    def clear(self):
        self.text1.delete("0","end")
        self.text2.delete("0","end")
        self.text3.delete("0","end")
        self.combo1.set("")


class Konstructtype(tk.Toplevel):
        def __init__(self,db):
            self.db=db
            super().__init__()
            self.dialog_on()
            self.view_type()

        def dialog_on(self):
            self.title("creat type")
            self.geometry('375x250')
            self.resizable(False,False)
            self.grab_set()
            self.focus_set()
            self.lbl1 = tk.Label(self, text="Название вида", font=("Arial Bold", 10))
            self.lbl1.place(x=1, y=1)
            self.text1 = ttk.Entry(self,width=30)
            self.text1.place(x=100, y=3)
            btn_ok=ttk.Button(self,text="Добавить",command= lambda: self.recordtype(self.text1.get()))
            btn_ok.place(x=1, y=25)



            self.lbl2 = tk.Label(self, text="Добавление подвида", font=("Arial Bold", 14))
            self.lbl2.place(x=1, y=75)
            self.lbl3 = tk.Label(self, text="Название вида", font=("Arial Bold", 10))
            self.lbl3.place(x=1, y=100)
            self.combo1 = ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_type)

            self.combo1.place(x=125,y=100)
            self.lbl4 = tk.Label(self, text="Название подвида", font=("Arial Bold", 10))
            self.lbl4.place(x=1, y=125)
            self.text2 = ttk.Entry(self,width=30)
            self.text2.place(x=125, y=125)
            self.lbl5 = tk.Label(self, text="Для кого", font=("Arial Bold", 10))
            self.lbl5.place(x=1, y=150)
            self.combo2 = ttk.Combobox(self,width=27,state="readonly")
            self.combo2['values']='Мужские','Женские','Унисекс'
            self.combo2.place(x=125,y=150)

            btn_ok1=ttk.Button(self,text="Добавить",command= lambda: self.recordsubtype(self.combo1.get(),
                                                                                        self.text2.get(),
                                                                                        self.combo2.get()))
            btn_ok1.place(x=1, y=175)
        def view_type(self):
            self.db.cursor.execute('''SELECT name FROM dept''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                self.data.append(row[0])
            self.combo1['values']=self.data
            return self.data
        def recordtype(self,name):
            self.db.insert_type(name)
        def recordsubtype(self,typename,subtypename,sex):
            self.db.insert_subtype(typename,subtypename,sex)



class Konstructshowcase(tk.Toplevel):
        def __init__(self,db):
            self.db=db
            super().__init__()
            self.dialog_on()
            self.view_showcase()


        def dialog_on(self):
            self.title("creat showcase")
            self.geometry('750x250')
            self.resizable(False,False)
            self.grab_set()
            self.focus_set()


            self.lbl1 = tk.Label(self, text="Название витрины", font=("Arial Bold", 10))
            self.lbl1.place(x=1, y=1)
            self.text1 = ttk.Entry(self,width=30)
            self.text1.place(x=125, y=3)


            self.lbl2 = tk.Label(self, text="Количество полок", font=("Arial Bold", 10))
            self.lbl2.place(x=1, y=30)
            self.spin1 = tk.Spinbox(self,from_=1,to=30, width=5)
            self.spin1.place(x=125,y=30)


            self.lbl3 = tk.Label(self, text="Вместимость полки", font=("Arial Bold", 10))
            self.lbl3.place(x=1, y=60)
            self.spin2 = tk.Spinbox(self,from_=1,to=30, width=5)
            self.spin2.place(x=125,y=60)

            btn_ok1=ttk.Button(self,text="Добавить",command= lambda: self.recordshowcase(self.text1.get(),
                                                                                        self.spin1.get(),
                                                                                        self.spin2.get()))
            btn_ok1.place(x=1, y=90)


            self.lbl3 = tk.Label(self, text="Уникальные полки", font=("Arial Bold", 15))
            self.lbl3.place(x=1, y=120)
            self.lbl4 = tk.Label(self, text="Витрина", font=("Arial Bold", 10))
            self.lbl4.place(x=1, y=150)
            self.combo1 = ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_showcase)
            self.combo1.place(x=125,y=150)
            self.lbl5 = tk.Label(self, text="Вместимость", font=("Arial Bold", 10))
            self.lbl5.place(x=1, y=180)
            self.spin3 = tk.Spinbox(self,from_=1,to=30, width=5)
            self.spin3.place(x=125,y=180)

            btn_ok2=ttk.Button(self,text="Добавить",command= lambda: self.recordshelf(self.combo1.get(),
                                                                                        self.spin3.get()

                                                                                        ))
            btn_ok2.place(x=1, y=210)




            self.lbl6 = tk.Label(self, text="Добавить витрине тип ", font=("Arial Bold", 15))
            self.lbl6.place(x=400, y=1)

            self.lbl6 = tk.Label(self, text="Выберите витрину ", font=("Arial Bold", 10))
            self.lbl6.place(x=400, y=38)
            self.combo2 = ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_showcase)
            self.combo2['values']=self.view_showcase()
            self.combo2.place(x=550,y=40)

            self.lbl7 = tk.Label(self, text="Выберите тип", font=("Arial Bold", 10))
            self.lbl7.place(x=400, y=68)
            self.combo3 = ttk.Combobox(self,width=27,state="readonly")
            self.combo3['values']=self.view_type()
            self.combo3.place(x=550,y=70)
            self.combo3.bind("<<ComboboxSelected>>",self.link)

            self.lbl8 = tk.Label(self, text="Выберите подтип", font=("Arial Bold", 10))
            self.lbl8.place(x=400, y=100)
            self.combo4 = ttk.Combobox(self,width=27,state="readonly")
            self.combo4.place(x=550,y=100)


            btn_ok1=ttk.Button(self,text="Добавить",command= lambda: self.recordtypeshowcase(self.combo2.get(),
                                                                                        self.combo4.get()))
            btn_ok1.place(x=400, y=120)





        def view_showcase(self):
            self.db.cursor.execute('''SELECT name FROM showcase''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                self.data.append(row[0])
            self.combo2['values']=self.data
            self.combo1['values']=self.data
            return self.data






        def recordshowcase (self,name,levelmax,kappa):
            self.db.insert_showcase(name,levelmax,kappa)


        def recordshelf (self,name,kappa):
            self.db.insert_shelf(name,kappa)


        def recordtypeshowcase(self,nameshowcase,namesubtype):
            self.data=[]
            self.k=0
            self.db.cursor.execute('''SELECT id FROM showcase where name = (%s)''', (nameshowcase,))
            self.id_showcase=int(str(self.db.cursor.fetchone()[0]))
            self.db.connection.commit()
            self.name=str(str(self.id_showcase)+" "+nameshowcase+" "+ namesubtype )
            try:
                self.db.cursor.execute('''SELECT name FROM subdept_showcase ''')
                for row in self.db.cursor.fetchall():
                    if row[0] == self.name:
                        self.k=self.k+1
                if self.k == 0:
                    self.db.inserttypeshowcase(nameshowcase,namesubtype)
                    messagebox.showinfo("Очень важно","Витрина добавлена")
                else:
                    messagebox.showinfo("Ошибка","Такая витрина уже есть")
            except:
                messagebox.showinfo("Ошибка","Данные были введены не коректно")
            return self.k


        def view_type(self):
            self.db.cursor.execute('''SELECT name FROM dept''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                self.data.append(row[0])
            return self.data

        def link(self,select):
            self.name=str(self.combo3.get())
            self.db.cursor.execute('''SELECT id FROM dept where name = (%s)''', (self.name,))
            self.id_dept=int(str((self.db.cursor.fetchone()[0])))
            self.date=[]
            self.db.cursor.execute('''select subdept.name   from dept
                                                                    inner join dept_subdept  ON dept_subdept.id_dept = dept.id
                                                                    inner join subdept on subdept.id=dept_subdept.id_subdept
                                                                    where dept.id=(%s)''', (self.id_dept,))
            self.data=[]
            for row in self.db.cursor.fetchall():
                self.data.append(row[0])
            self.combo4['values']=self.data
            return self.data


class Konstructsubdeparament(tk.Toplevel):
        def __init__(self,db):
            self.db=db
            super().__init__()
            self.dialog_on()




        def dialog_on(self):
            self.title("creat subdepartament")
            self.geometry('400x300')
            self.resizable(False,False)
            self.grab_set()
            self.focus_set()




            self.lbl1 = tk.Label(self, text="Добавить подотдел", font=("Arial Bold", 15))
            self.lbl1.place(x=1, y=1)
            self.lbl2 = tk.Label(self, text="Название подотдела", font=("Arial Bold", 10))
            self.lbl2.place(x=1, y=40)
            self.text1 = ttk.Entry(self,width=30)
            self.text1.place(x=150, y=40)
            self.lbl3 = tk.Label(self, text="Витрина", font=("Arial Bold", 10))
            self.lbl3.place(x=1, y=70)
            self.combo1= ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_typeshowcase)
            self.combo1.place(x=150,y=70)
            self.lbl7 = tk.Label(self, text="Для кого", font=("Arial Bold", 10))
            self.lbl7.place(x=1, y=100)
            self.combo4 = ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_typeshowcase)
            self.combo4.place(x=150,y=100)
            self.combo4['values'] = ("Унисекс","Мужские","Женские")
            self.combo4.set("Унисекс")

            btn_ok1=ttk.Button(self,text="Добавить",command= lambda: self.record_subdepartament(self.text1.get(),self.combo1.get(),self.combo4.get()))
            btn_ok1.place(x=1, y=130)



            self.lbl4 = tk.Label(self, text="Добавить витрину в отдел  ", font=("Arial Bold", 15))
            self.lbl4.place(x=1, y=170)
            self.lbl5 = tk.Label(self, text="Отдел", font=("Arial Bold", 10))
            self.lbl5.place(x=1, y=200)
            self.combo2= ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_subdept)
            self.combo2.place(x=150,y=200)
            self.lbl6 = tk.Label(self, text="Витрина", font=("Arial Bold", 10))
            self.lbl6.place(x=1, y=230)
            self.combo3 = ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_typeshowcase)
            self.combo3.place(x=150,y=230)

            btn_ok2=ttk.Button(self,text="Добавить",command= lambda: self.update_subdepartament2(self.combo2.get(),self.combo3.get()))
            btn_ok2.place(x=1, y=260)


        def view_typeshowcase(self):
            self.db.cursor.execute('''SELECT name FROM subdept_showcase''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                self.data.append(row[0])
            self.combo1['values']=self.data
            self.combo3['values']=self.data
            return self.data

        def view_subdept(self):
            self.db.cursor.execute('''SELECT name FROM depttype''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                if row[0] not in self.data:
                    self.data.append(row[0])
            self.combo2['values']=self.data
            return self.data

        def record_subdepartament(self,name,name_showcase,sex):
            self.data=[]
            self.k=0
            self.db.cursor.execute('''SELECT id FROM subdept_showcase where name = (%s)''', (name_showcase,))
            self.id_depttype=int(str(self.db.cursor.fetchone()[0]))
            self.db.connection.commit()
            self.name=str(str(self.id_depttype)+" "+name)
            self.db.cursor.execute('''SELECT name FROM depttype ''')
            for row in self.db.cursor.fetchall():
                if row[0] == self.name:
                    self.k=self.k+1
            if self.k == 0:
                self.db.insert_subdepartament(name,name_showcase,sex)
                self.view_typeshowcase()
                self.view_subdept()
                messagebox.showinfo("Очень важно","Отдел добавлен")
            else:
                messagebox.showinfo("Ошибка","Такой отдел уже есть")

                # messagebox.showinfo("Ошибка","Данные были введены не коректно")
            return self.k

        def update_subdepartament(self,name,name_showcase):
            self.data=[]
            self.k=0
            self.db.cursor.execute('''SELECT id FROM subdept_showcase where name = (%s)''', (name_showcase,))
            self.id_depttype=int(str(self.db.cursor.fetchone()[0]))
            self.db.connection.commit()
            self.name=str(str(self.id_depttype)+" "+name)
            self.db.cursor.execute('''SELECT name FROM depttype ''')
            for row in self.db.cursor.fetchall():
                if row[0] == self.name:
                    self.k=self.k+1
            if self.k == 0:
                self.db.insert_subdepartament(name,name_showcase)
                self.view_typeshowcase()
                self.view_subdept()
                messagebox.showinfo("Очень важно","Витрина")
            else:
                messagebox.showinfo("Ошибка","Такая витрина уже есть")

                # messagebox.showinfo("Ошибка","Данные были введены не коректно")
            return self.k

class Konstructdeparament(tk.Toplevel):
        def __init__(self,db):
            self.db=db
            super().__init__()
            self.dialog_on()


        def dialog_on(self):
            self.title("creat departament")
            self.geometry('400x300')
            self.resizable(False,False)
            self.grab_set()
            self.focus_set()
            self.lbl1 = tk.Label(self, text="Добавить отдел ", font=("Arial Bold", 15))
            self.lbl1.place(x=1, y=1)
            self.lbl2 = tk.Label(self, text="Магазин", font=("Arial Bold", 10))
            self.lbl2.place(x=1, y=40)
            self.combo1= ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_shop)
            self.combo1.place(x=150,y=40)
            self.lbl3 = tk.Label(self, text="Название отдела", font=("Arial Bold", 10))
            self.lbl3.place(x=1, y=70)
            self.text1 = ttk.Entry(self,width=30)
            self.text1.place(x=150, y=70)
            self.lbl4 = tk.Label(self, text="Подотдел", font=("Arial Bold", 10))
            self.lbl4.place(x=1, y=100)
            self.combo2= ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_subdept)
            self.combo2.place(x=150,y=100)

            btn_ok1=ttk.Button(self,text="Добавить",command= lambda: self.record_departament(self.combo1.get(),self.text1.get(),self.combo2.get()))
            btn_ok1.place(x=1, y=130)



            self.lbl5 = tk.Label(self, text="Добавить подотдел ", font=("Arial Bold", 15))
            self.lbl5.place(x=1, y=170)
            self.lbl6 = tk.Label(self, text="Отдел", font=("Arial Bold", 10))
            self.lbl6.place(x=1, y=200)
            self.combo3= ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_dept)
            self.combo3.place(x=150,y=200)
            self.lbl7 = tk.Label(self, text="Добавить подотдел ", font=("Arial Bold", 10))
            self.lbl7.place(x=1, y=230)
            self.combo4= ttk.Combobox(self,width=27,state="readonly",postcommand=self.view_subdept)
            self.combo4.place(x=150,y=230)

            btn_ok2=ttk.Button(self,text="Добавить",command= lambda: self.update_departament(self.combo3.get(),self.combo4.get()))
            btn_ok2.place(x=1, y=260)



        def record_departament(self,shop,name,subname):
            self.data=[]
            self.k=0
            self.db.cursor.execute('''SELECT id FROM shop where address = (%s)''', (shop,))
            self.id_shop=int(str(self.db.cursor.fetchone()[0]))
            self.db.connection.commit()
            self.name=str(str(self.id_shop)+" "+name)
            self.db.cursor.execute('''SELECT name FROM depttype ''')
            for row in self.db.cursor.fetchall():
                if row[0] == self.name:
                    self.k=self.k+1
            if self.k == 0:
                self.db.insert_departament(shop,name,subname)
                messagebox.showinfo('Очень важно', 'Отдел успешно добавлен')
                self.text1.delete("0","end")
                self.combo1.set("")
                self.combo2.set("")
            else:
                messagebox.showinfo("Ошибка","Такой отдел уже есть")
            return self.k


        def update_departament(self,namedep,namesubdep):
            self.db.update_departament(namedep,namesubdep)
            messagebox.showinfo('Очень важно', 'Подотдел успешно добавлен')

            self.combo3.set("")
            self.combo4.set("")


        def view_shop(self):
            self.db.cursor.execute('''SELECT address FROM shop''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                if row[0] not in self.data:
                    self.data.append(row[0])
            self.combo1['values']=self.data
            return self.data

        def view_subdept(self):
            self.db.cursor.execute('''SELECT name FROM depttype''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                self.data.append(row[0])
            self.combo2['values']=self.data
            self.combo4['values']=self.data
            return self.data

        def view_dept(self):
            self.db.cursor.execute('''SELECT name FROM departament''')
            self.data=[]
            for row in self.db.cursor.fetchall():
                if row[0] not in self.data:
                    self.data.append(row[0])
            self.combo3['values']=self.data
            return self.data

class Merch(tk.Toplevel):
    def __init__(self,window,a,app,db):
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
        # self.view()

        Btn_window1=tk.Button(self,text='Войти', command = lambda:self.autarization(self.combo.get()))
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
        try:
            self.db.cursor.execute('''SELECT id FROM shop where address = (%s)''',(nameshop,))
            self.id_shop=int(self.db.cursor.fetchone()[0])
            self.a.destroy()
            Main(self.view,self.app,self.id_shop)
            self.destroy()
        except:
            messagebox.showinfo('Ошибка', 'Выберите имя магазина')


combo=("Магазин","Сотрудники","Виды","Витрины","Подотделы","Отделы")
