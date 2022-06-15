import tkinter as tk
from tkinter import ttk,messagebox
from insert_db import Db
from New import New

class Task(tk.Toplevel):
    def __init__(self,window,id_shop):
        super().__init__()
        self.db=db
        self.id_shop= id_shop
        self.view=window
        self.open_dialog()

    def open_dialog(self):
        self.title("Merchendaiser - Создать задачу")
        self.geometry('230x400')
        self.resizable(False,False)


        self.zag1 = tk.Label(self, text="Выберите витрину", font=("Arial Bold", 10))
        self.zag1.place(x=1, y=1)
        self.combo1 = ttk.Combobox(self,width=27,state="readonly")
        self.combo1['values']=self.view_type()
        self.combo1.place(x=10, y=20)
        self.combo1.bind("<<ComboboxSelected>>",self.link)
        self.combo2 = ttk.Combobox(self,width=27,state="readonly")
        self.combo2['values']
        self.combo2.place(x=10, y=50)
        self.combo2.bind("<<ComboboxSelected>>",self.link_showcase)
        self.combo3 = ttk.Combobox(self,width=27,state="readonly")
        self.combo3['values']
        self.combo3.place(x=10, y=80)


        self.status1=tk.IntVar()
        self.status1.set(1)
        self.chek1 = tk.Checkbutton(self, text='Учитывать вид обуви ветрины',variable= self.status1, onvalue=1, offvalue=0)
        self.chek1.place(x=1, y=110)
        self.status2=tk.IntVar()
        self.status2.set(1)
        self.chek2 = tk.Checkbutton(self, text='Учитывать пол подотдела',variable= self.status2, onvalue=1, offvalue=0)
        self.chek2.place(x=1, y=140)

        self.zag2 = tk.Label(self, text="Выберите необходимые параметры :", font=("Arial Bold", 10))
        self.zag2.place(x=1, y=170)
        self.combo4 = ttk.Combobox(self,width=27,state="readonly")
        self.combo4['values']
        self.combo4.place(x=10, y=210)
        self.combo5 = ttk.Combobox(self,width=27,state="readonly")
        self.combo5['values']
        self.combo5.place(x=10, y=240)
        self.combo6 = ttk.Combobox(self,width=27,state="readonly")
        self.combo6['values']
        self.combo6.place(x=10, y=270)
        self.combo4.set("Бренды")
        self.combo5.set("Цвета")
        self.combo6.set("Сезоны")
        self.db.cursor.execute('''SELECT name FROM vendor''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        self.combo4['values']=self.data
        self.combo5['values']=color
        self.combo6['values']=("Летний","Зимний","Весене-осенний")

        Btn_clear=tk.Button(self,text='Отчистить ', command= self.clear)
        Btn_clear.place(x=10,y=300)
        Btn_asuslegen=tk.Button(self,text='Произвести выкладку', command= lambda: self.auto_asuslegen(self.combo1.get(),self.combo2.get(),self.combo3.get(),self.combo4.get(),self.combo5.get(),self.combo6.get(),self.status1.get(),self.status2.get()))
        Btn_asuslegen.place(x=10,y=360)

    def auto_asuslegen(self,departament,subdept,showcase,brand,color,season,st1,st2):
        try:
            if brand == "Бренды" and color == "Цвета" and  season == "Сезоны":
                messagebox.showinfo('Ошибка', 'Выберите хотя бы один параметр')
            else:
                New(self.view,self.id_shop,departament,subdept,showcase,brand,color,season,st1,st2)
        except:
            messagebox.showinfo('Ошибка', 'Выберите ветрину')

    def link(self,select):

        self.name=str(self.combo1.get())
        self.db.cursor.execute('''SELECT id FROM departament where name = (%s) ''', (self.name,))

        self.id_departament = int(str(self.db.cursor.fetchone()[0]))

        self.combo2.set("")
        self.combo3.set("")
        self.db.cursor.execute('''select depttype."name" from departament
        inner join depttype  on depttype.id = departament.id_depttype where departament.id_shop=(%s) and departament.name=(%s) ''', (self.id_shop,self.name,))
        self.data=[]

        for row in self.db.cursor.fetchall():
            if row[0] not in self.data:
                self.data.append(row[0])
        self.combo2['values']=self.data
        return self.data

    def link_showcase(self,select):
        self.combo3.set("")
        self.db.cursor.execute('''SELECT id FROM depttype where name = (%s) ''', (self.combo2.get(),))
        self.id_subdepartament = int(str(self.db.cursor.fetchone()[0]))
        self.db.cursor.execute('''select subdept_showcase.name from depttype
inner join subdept_showcase  ON depttype.id_subdept  = subdept_showcase.id
inner join departament ON depttype.id=departament.id_depttype where depttype.id=(%s)  ''', (self.id_subdepartament,))
        self.data=[]
        for row in self.db.cursor.fetchall():
            if row[0] not in self.data:
                self.data.append(row[0])
        self.combo3['values']=self.data
        return self.data

    def view_type(self):
        self.db.cursor.execute('''SELECT name FROM departament where id_shop = (%s)''',(self.id_shop,))
        self.data=[]
        for row in self.db.cursor.fetchall():
            if row[0] not in self.data:
                self.data.append(row[0])
        return self.data

    def clear (self):
        self.combo4.set("Бренды")
        self.combo5.set("Цвета")
        self.combo6.set("Сезоны")
        self.db.cursor.execute('''SELECT name FROM vendor''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        self.combo4['values']=self.data
        self.combo5['values']=color
        self.combo6['values']=("Летний","Зимний","Весене-осенний")

color=['Хром','Белый','Чёрный','Шоколадный',
'Серый','Тёмно-серый','Зеленный','Тёмно-зелный',
'Синий','Тёмно-синий','Красный','Бордовый',
'Оранжевый','Жёльтый','Бежевый','Розовый','Коричневый','Хаки','Камуфляж']

db=Db()
