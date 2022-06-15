import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import Calendar,DateEntry
from datetime import date
from insert_db import Db
from Vendor import Vendor


class Shoes(tk.Toplevel):
    def __init__(self,window,id_shop):
        super().__init__()
        self.db=db
        self.id_shop= id_shop
        self.view=window
        self.open_dialog()



    def open_dialog(self):
        self.title('Merchendaiser - склад ')
        self.geometry('820x400')
        self.resizable(False,False)
        self.grab_set()

        self.text1 = ttk.Entry(self,width=55)
        self.text1.place(x=1,y=3)
        btn_search=ttk.Button(self,text="Поиск",command= lambda:self.search(self.text1.get()))
        btn_search.pack(fill="y")
        btn_view=ttk.Button(self,text="Показать всё",command= self.view_records)
        btn_view.place(x=470,y=1)

        self.tree= ttk.Treeview(self,columns=('ID','name','sh_type','count','color','material','season','size','vendor','d_data','discount','price'),height=15,  show='headings')
        self.tree.column('ID', width=20, anchor=tk.CENTER)
        self.tree.column('name', width=80, anchor=tk.CENTER)
        self.tree.column('sh_type', width=90, anchor=tk.CENTER)
        self.tree.column('count', width=60, anchor=tk.CENTER)
        self.tree.column('color', width=80, anchor=tk.CENTER)
        self.tree.column('material', width=80, anchor=tk.CENTER)
        self.tree.column('season', width=70, anchor=tk.CENTER)
        self.tree.column('size', width=60, anchor=tk.CENTER)
        self.tree.column('vendor', width=80, anchor=tk.CENTER)
        self.tree.column('d_data', width=50, anchor=tk.CENTER)
        self.tree.column('discount', width=60, anchor=tk.CENTER)
        self.tree.column('price', width=50, anchor=tk.CENTER)

        self.tree.heading('ID',text='ID')
        self.tree.heading('name',text='Название')
        self.tree.heading('sh_type',text='Тип обуви')
        self.tree.heading('count',text='Кол-во')
        self.tree.heading('color',text='цвет')
        self.tree.heading('material',text='Материал')
        self.tree.heading('season',text='Сезон')
        self.tree.heading('size',text='Размер')
        self.tree.heading('vendor',text='Бренд')
        self.tree.heading('d_data',text='Дата п.')
        self.tree.heading('discount',text='Скидка')
        self.tree.heading('price',text='Цена')


        self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
        self.tree.configure(yscroll=self.ysb.set)
        self.ysb.pack(side=tk.RIGHT,fill="y")
        self.tree.pack(fill="x")



        btn_add=ttk.Button(self,text="Добвить",command=self.add_shoes)
        btn_add.pack(side=tk.LEFT,fill="y")
        btn_update=ttk.Button(self,text="Изменить",command=self.update_shoes)
        btn_update.pack(side=tk.LEFT,fill="y")
        btn_delete=ttk.Button(self,text="Удалить как ошибку",command=self.delet)
        btn_delete.pack(side=tk.LEFT,fill="y")
        Btn_add_onshelf=ttk.Button(self,text="Добвить товар на полку ",command=self.add_onshelf)
        Btn_add_onshelf.pack(side=tk.LEFT,fill="y")
        Btn_write_off=ttk.Button(self,text="Списать товар",command=self.write_off)
        Btn_write_off.pack(side=tk.LEFT,fill="y")
        btn_close=ttk.Button(self,text="Закрыть",command=self.destroy)
        btn_close.pack(side=tk.RIGHT,fill="y")
        self.b=self.view_records()


    def search(self,search):
        self.db.cursor.execute('''select shoes.id ,shoes.name,shoes.sh_type,shoes.count, c.color, shoes.material,shoes.season, s.size, v.name as vendor, vs.de_date,shoes.discount,shoes.price from shoes
inner join color  c  ON c.id_shoes  = shoes.id
inner join size  s on s.id_shoes = shoes.id
inner join  vendor_shoes  vs on vs.id_shoes = shoes.id
inner join vendor v  on v.id = vs.id_vendor
inner join warehouse_shoes on warehouse_shoes.id_shoes =shoes.id
inner join warehouse on warehouse.id = warehouse_shoes.id_warehouse
inner join shop on shop.id = warehouse.id_shop
where shop.id = (%s) and shoes.status=False and shoes.count != 0 and shoes.name LIKE %s
                                ''',(self.id_shop,search,))
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]



    def write_off(self):
        try:
            self.id_shoes=self.tree.set(self.tree.selection()[0], '#1')
            self.db.cursor.execute('''select id_shoes from trash where id_shoes=(%s) ''',(self.id_shoes,))
            if self.db.cursor.fetchone() is None :
                self.db.cursor.execute('''insert into trash (id_shoes,tr_data) values (%s,%s) ''',(self.id_shoes,date.today(),))
            self.db.cursor.execute('''update shoes set count = count-1 ,count_writeoff=count_writeoff+1  where id = (%s) ''', (self.id_shoes,))
            self.view_records()
            messagebox.showinfo('Очень важно', 'Товар списан')

        except:
            messagebox.showinfo('Ошибка', 'Выберите товар')




    def add_onshelf(self):
        try:
            self.id_shoes=self.tree.set(self.tree.selection()[0], '#1')
            Add_onshelf(self.id_shoes,self.view,self.id_shop)
            self.destroy()
        except:
            messagebox.showinfo('Ошибка', 'Выберите товар')

    def add_shoes(self):
        self.destroy()
        Reception(self.view,self.id_shop)


    def update_shoes(self):
        try:
            self.id_update=self.tree.set(self.tree.selection()[0], '#1')
            Update_shoes(self.view,self.id_shop,self.id_update)
            self.destroy()
        except:
            messagebox.showinfo('Ошибка', 'Выберите товар')

    def delet(self):
        try:
            self.id_delet=self.tree.set(self.tree.selection()[0], '#1')
            self.db.cursor.execute(''' delete from warehouse_shoes where id_shoes=(%s)''',(self.id_delet,))
            self.db.cursor.execute(''' delete from vendor_shoes where id_shoes=(%s)''',(self.id_delet,))
            self.db.cursor.execute(''' delete from size where id_shoes=(%s)''',(self.id_delet,))
            self.db.cursor.execute(''' delete from color where id_shoes=(%s)''',(self.id_delet,))
            self.db.cursor.execute(''' delete from shoes_shelf where id_shoes=(%s)''',(self.id_delet,))
            self.db.cursor.execute(''' delete from shoes where id=(%s)''',(self.id_delet,))
            self.view_records()
        except:
            messagebox.showinfo('Ошибка', 'Выберите товар')

    def view_records(self):
        self.db.cursor.execute('''select shoes.id ,shoes.name,shoes.sh_type,shoes.count, c.color, shoes.material, shoes.season,s.size, v.name as vendor, vs.de_date,shoes.discount,shoes.price from shoes
inner join color  c  ON c.id_shoes  = shoes.id
inner join size  s on s.id_shoes = shoes.id
inner join  vendor_shoes  vs on vs.id_shoes = shoes.id
inner join vendor v  on v.id = vs.id_vendor
inner join warehouse_shoes on warehouse_shoes.id_shoes =shoes.id
inner join warehouse on warehouse.id = warehouse_shoes.id_warehouse
inner join shop on shop.id = warehouse.id_shop
where shop.id = (%s) and shoes.status=False and shoes.count != 0 order by shoes.id DESC
                                ''',(self.id_shop,))
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]



class Reception (tk.Toplevel):
    def __init__(self,window,id_shop):
        super().__init__(window)
        self.view=window
        self.db=db
        self.id_shop=id_shop
        self.b=Shoes(self.view,self.id_shop)
        self.__acceptance()


    def __acceptance(self):
        self.title('Окно приёма нового товара ')
        self.geometry('700x280')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()

        self.zag1 = tk.Label(self, text="Основные параметры:", font=("Arial Bold", 15))
        self.zag1.place(x=1, y=1)
        self.lbl1 = tk.Label(self, text="Название обуви", font=("Arial Bold", 10))
        self.lbl1.place(x=1, y=30)
        self.text1 = ttk.Entry(self,width=30)
        self.text1.place(x=125, y=30)

        self.lbl2 = tk.Label(self, text="Выберите тип", font=("Arial Bold", 10))
        self.lbl2.place(x=1, y=60)
        self.combo1 = ttk.Combobox(self,width=27,state="readonly")
        self.combo1['values'] =self.view_type()
        self.combo1.place(x=125, y=60)
        self.combo1.bind("<<ComboboxSelected>>",self.link)

        self.lbl2 = tk.Label(self, text="Выберите под тип", font=("Arial Bold", 10))
        self.lbl2.place(x=1, y=90)
        self.combo2 = ttk.Combobox(self,width=27,state="readonly")
        self.combo2['values']
        self.combo2.place(x=125, y=90)

        self.zag2 = tk.Label(self, text="Дополнительные параметры:", font=("Arial Bold", 15))
        self.zag2.place(x=340, y=1)

        self.lbl3 = tk.Label(self, text="Выберите цвет", font=("Arial Bold", 10))
        self.lbl3.place(x=350, y=30)
        self.combo3 = ttk.Combobox(self,width=27,state="readonly")
        self.combo3['values']=color
        self.combo3.place(x=475, y=35)


        self.lbl4 = tk.Label(self, text="Выберите материал", font=("Arial Bold", 10))
        self.lbl4.place(x=350, y=60)
        self.combo4 = ttk.Combobox(self,width=27,state="readonly",)
        self.combo4['values']=material
        self.combo4.place(x=475, y=65)
        self.lbl10 = tk.Label(self, text="Выберите сезон", font=("Arial Bold", 10))
        self.lbl10.place(x=350, y=90)
        self.combo6 = ttk.Combobox(self,width=27,state="readonly",)
        self.combo6['values']=("Летний","Зимний","Весене-осенний")
        self.combo6.place(x=475, y=95)

        self.lbl5 = tk.Label(self, text="Выберите размер", font=("Arial Bold", 10))
        self.lbl5.place(x=350, y=120)
        self.spin1 = tk.Spinbox(self,from_=20,to=60, width=5)
        self.spin1.place(x=475,y=120)

        self.lbl5 = tk.Label(self, text="Кол-во:", font=("Arial Bold", 10))
        self.lbl5.place(x=505, y=120)
        self.spin4 = tk.Spinbox(self,from_=1,to=100, width=5)
        self.spin4.place(x=555,y=120)

        self.zag3 = tk.Label(self, text="Бренд:", font=("Arial Bold", 15))
        self.zag3.place(x=1, y=150)

        self.lbl6 = tk.Label(self, text="Поставщик", font=("Arial Bold", 10))
        self.lbl6.place(x=1, y=180)
        self.combo5 = ttk.Combobox(self,width=27,state="readonly", postcommand=self.view_vendor)
        self.combo5['values']
        self.combo5.place(x=125, y=180)



        self.lbl7 = tk.Label(self, text="Дата поставки", font=("Arial Bold", 10))
        self.lbl7.place(x=1, y=210)
        self.cal1 = DateEntry(self,width=27,year=2022)
        self.cal1.config(headersbackground='#364c55',foreground='#000',background='#fff')
        self.cal1.place(x=125,y=210)


        self.zag3 = tk.Label(self, text="Цена:", font=("Arial Bold", 15))
        self.zag3.place(x=340, y=150)

        self.lbl8 = tk.Label(self, text="Цена", font=("Arial Bold", 10))
        self.lbl8.place(x=350, y=180)
        self.spin2 = tk.Spinbox(self,from_=1,to=1000000, width=10)
        self.spin2.place(x=475,y=180)


        self.lbl9 = tk.Label(self, text="Скидка в %", font=("Arial Bold", 10))
        self.lbl9.place(x=350, y=210)
        self.spin3 = tk.Spinbox(self,from_=0,to=100, width=5)
        self.spin3.place(x=475,y=210)


        btn_ok=ttk.Button(self,text="Добавить",command= lambda:self.record_shoes(self.text1.get(),
                                                                                  self.combo2.get(),
                                                                                  self.combo3.get(),
                                                                                  self.combo4.get(),
                                                                                  self.combo6.get(),
                                                                                  self.spin1.get(),
                                                                                  self.combo5.get(),
                                                                                  self.cal1.get_date(),
                                                                                  self.spin2.get(),
                                                                                  self.spin3.get(),
                                                                                  self.spin4.get(),
                                                                                  self.id_shop))

        btn_ok.place(x=1, y=240)


        btn_vendor=ttk.Button(self,text="Добавить парметры",command=self.add_vendor)
        btn_vendor.place(x=120, y=240)
        btn_close=ttk.Button(self,text="Закрыть",command=self.destroy)
        btn_close.place(x=600, y=240)



    def add_vendor(self):
        Vendor(self.view)


    def record_shoes(self,name,subtype,color,material,season,size,vendor,d_vendor,price,discount,count,id_shop,):
        try:
            self.db.insert_shoes(name,subtype,color,material,season,size,vendor,d_vendor,price,discount,count,id_shop)
            self.clear()
            self.b.view_records()
            messagebox.showinfo('Очень важно', 'Выполнено')
        except:
            messagebox.showinfo('Ошибка', 'Не все данные занесены или занесены не корректно')






    def view_type(self):
        self.db.cursor.execute('''SELECT name FROM dept''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        return self.data

    def link(self,select):
        self.name=str(self.combo1.get())
        self.combo2.set("")
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
        self.combo2['values']=self.data
        return self.data

    def view_vendor(self):
        self.combo5.set("")
        self.db.cursor.execute('''SELECT name FROM vendor''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        self.combo5['values'] = self.data
        return self.data

    def clear(self):
        self.text1.delete("0","end")
        self.combo1.set("")
        self.combo2.set("")
        self.combo3.set("")
        self.combo4.set("")
        self.combo5.set("")


class Update_shoes(tk.Toplevel):
    def __init__(self,window,id_shop,id_update):
        super().__init__(window)
        self.db= db
        self.id_shoes=id_update
        self.id_update = id_update
        self.id_shop= id_shop
        self.view=window
        self.b=Shoes(self.view,self.id_shop)
        self.open_dialog()



    def open_dialog(self):
        self.title('Изменение ')
        self.geometry('750x300')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()


        self.zag1 = tk.Label(self, text="Основные параметры:", font=("Arial Bold", 15))
        self.zag1.place(x=1, y=1)
        self.lbl1 = tk.Label(self, text="Название обуви", font=("Arial Bold", 10))
        self.lbl1.place(x=1, y=30)
        self.text1 = ttk.Entry(self,width=30)
        self.text1.place(x=125, y=30)

        self.lbl2 = tk.Label(self, text="Выберите тип", font=("Arial Bold", 10))
        self.lbl2.place(x=1, y=60)
        self.combo1 = ttk.Combobox(self,width=27,state="readonly")
        self.combo1['values'] =self.view_type()
        self.combo1.place(x=125, y=60)
        self.combo1.bind("<<ComboboxSelected>>",self.link)

        self.lbl2 = tk.Label(self, text="Выберите под тип", font=("Arial Bold", 10))
        self.lbl2.place(x=1, y=90)
        self.combo2 = ttk.Combobox(self,width=27,state="readonly")
        self.combo2['values']
        self.combo2.place(x=125, y=90)

        self.zag2 = tk.Label(self, text="Дополнительные параметры:", font=("Arial Bold", 15))
        self.zag2.place(x=340, y=1)

        self.lbl3 = tk.Label(self, text="Выберите цвет", font=("Arial Bold", 10))
        self.lbl3.place(x=350, y=30)
        self.combo3 = ttk.Combobox(self,width=27,state="readonly")
        self.combo3['values']=color
        self.combo3.place(x=475, y=35)


        self.lbl4 = tk.Label(self, text="Выберите материал", font=("Arial Bold", 10))
        self.lbl4.place(x=350, y=60)
        self.combo4 = ttk.Combobox(self,width=27,state="readonly",)
        self.combo4['values']=material
        self.combo4.place(x=475, y=65)
        self.lbl10 = tk.Label(self, text="Выберите сезон", font=("Arial Bold", 10))
        self.lbl10.place(x=350, y=90)
        self.combo6 = ttk.Combobox(self,width=27,state="readonly",)
        self.combo6['values']=("Летний","Зимний","Весене-осенний")
        self.combo6.place(x=475, y=95)

        self.lbl5 = tk.Label(self, text="Выберите размер", font=("Arial Bold", 10))
        self.lbl5.place(x=350, y=120)
        self.spin1 = tk.Spinbox(self,from_=20,to=60, width=5)
        self.spin1.place(x=475,y=120)

        self.lbl5 = tk.Label(self, text="Кол-во:", font=("Arial Bold", 10))
        self.lbl5.place(x=505, y=120)
        self.spin4 = tk.Spinbox(self,from_=1,to=100, width=5)
        self.spin4.place(x=555,y=120)

        self.zag3 = tk.Label(self, text="Бренд:", font=("Arial Bold", 15))
        self.zag3.place(x=1, y=150)

        self.lbl6 = tk.Label(self, text="Поставщик", font=("Arial Bold", 10))
        self.lbl6.place(x=1, y=180)
        self.combo5 = ttk.Combobox(self,width=27,state="readonly", postcommand=self.view_vendor)
        self.combo5['values']
        self.combo5.place(x=125, y=180)



        self.lbl7 = tk.Label(self, text="Дата поставки", font=("Arial Bold", 10))
        self.lbl7.place(x=1, y=210)
        self.cal1 = DateEntry(self,width=27,year=2022)
        self.cal1.config(headersbackground='#364c55',foreground='#000',background='#fff')
        self.cal1.place(x=125,y=210)


        self.zag3 = tk.Label(self, text="Цена:", font=("Arial Bold", 15))
        self.zag3.place(x=340, y=150)

        self.lbl8 = tk.Label(self, text="Цена", font=("Arial Bold", 10))
        self.lbl8.place(x=350, y=180)
        self.spin2 = tk.Spinbox(self,from_=1,to=1000000, width=10)
        self.spin2.place(x=475,y=180)


        self.lbl9 = tk.Label(self, text="Скидка в %", font=("Arial Bold", 10))
        self.lbl9.place(x=350, y=210)
        self.spin3 = tk.Spinbox(self,from_=0,to=100, width=5)
        self.spin3.place(x=475,y=210)
        self.normal()

        btn_ok=ttk.Button(self,text="Изменить", command=lambda:self.update_shoes(self.text1.get(),
                                                                                self.combo2.get(),
                                                                                self.combo3.get(),
                                                                                self.combo4.get(),
                                                                                self.combo6.get(),
                                                                                self.spin1.get(),
                                                                                self.spin4.get(),
                                                                                self.combo5.get(),
                                                                                self.cal1.get_date(),
                                                                                self.spin2.get(),
                                                                                self.spin3.get()))
        btn_ok.place(x=1, y=240)

        btn_close=ttk.Button(self,text="Закрыть",command=self.destroy)
        btn_close.place(x=100, y=240)

    def update_shoes(self,name,subtype,color,material,season,size,count,vendor,d_vendor,price,discount):
        try:
            self.db.cursor.execute('''UPDATE shoes SET name=(%s),sh_type=(%s),count=(%s),price=(%s),discount=(%s),material=(%s),season=(%s) WHERE id=(%s); ''',
                                                        (name,subtype,count,price,discount,material,season,self.id_shoes,))

            self.db.cursor.execute('''UPDATE color SET color=(%s)  WHERE id_shoes=(%s); ''',
                                                        (color,self.id_shoes,))

            self.db.cursor.execute('''UPDATE size SET size=(%s)  WHERE id_shoes=(%s); ''',
                                                        (size,self.id_shoes,))

            self.db.cursor.execute('''SELECT id_vendor from vendor_shoes where id_shoes =(%s)''',(self.id_shoes,))


            self.id_vendor=int(str(self.db.cursor.fetchone()[0]))

            self.db.cursor.execute('''SELECT id from Vendor where name =(%s)''',(vendor,))
            self.new_id_vendor=int(str(self.db.cursor.fetchone()[0]))

            self.db.cursor.execute('''UPDATE vendor_shoes SET id_vendor=(%s),de_date=(%s)  WHERE id_shoes=(%s) and id_vendor=(%s); ''',
                                                        (self.new_id_vendor,d_vendor,self.id_shoes,self.id_vendor,))
            self.b.view_records()
            messagebox.showinfo('Очень важно', 'Изменения сохранены')

            self.destroy()
        except:
            messagebox.showinfo('Ошибка', 'Не все данные занесены или занесены не корректно')

    def normal (self):

        self.data=[]
        self.db.cursor.execute('''select shoes.id ,shoes.name,shoes.sh_type,shoes.count, c.color, shoes.material, s.size, v.name as vendor, vs.de_date,shoes.discount,shoes.price,shoes.season from shoes
inner join color  c  ON c.id_shoes  = shoes.id
inner join size  s on s.id_shoes = shoes.id
inner join  vendor_shoes  vs on vs.id_shoes = shoes.id
inner join vendor v  on v.id = vs.id_vendor
inner join warehouse_shoes on warehouse_shoes.id_shoes =shoes.id
inner join warehouse on warehouse.id = warehouse_shoes.id_warehouse
inner join shop on shop.id = warehouse.id_shop
where shop.id = (%s) and shoes.status=False and shoes.id=(%s)
                                ''',(self.id_shop,self.id_update,))
        for row in self.db.cursor.fetchall():
            self.data=row

        self.text1.insert(0,self.data[1])
        self.combo2.set(str(self.data[2]))
        self.spin4.delete(0)
        self.spin4.insert(0,int(self.data[3]))
        self.combo3.set(str(self.data[4]))
        self.combo4.set(str(self.data[5]))
        self.spin1.delete(0)
        self.spin1.insert(0,float(self.data[6]))
        self.combo5.set(str(self.data[7]))
        self.spin3.delete(0)
        self.spin3.insert(0,int(self.data[9]))
        self.spin2.delete(0)
        self.spin2.insert(0,float(self.data[10]))
        self.combo6.set(str(self.data[11]))
        return self.data

    def view_type(self):
        self.db.cursor.execute('''SELECT name FROM dept''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        return self.data

    def link(self,select):
        self.name=str(self.combo1.get())
        self.combo2.set("")
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
        self.combo2['values']=self.data
        return self.data
    def view_vendor(self):
        self.combo5.set("")
        self.db.cursor.execute('''SELECT name FROM vendor''')
        self.data=[]
        for row in self.db.cursor.fetchall():
            self.data.append(row[0])
        self.combo5['values'] = self.data
        return self.data

class Add_onshelf(tk.Toplevel):
    def __init__(self,id_shoes,window,id_shop):
        super().__init__(window)
        self.db= db
        self.id_shop= id_shop
        self.view=window
        self.id_shoes=id_shoes
        self.b=Shoes(self.view,self.id_shop)
        self.open_dialog()

    def open_dialog(self):
        self.title('Добавлеие товара на полку')
        self.geometry('200x200')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()
        self.lbl1 = tk.Label(self, text=self.shoes_name(), font=("Arial Bold", 10))
        self.lbl1.place(x=10, y=10)



        self.combo1 = ttk.Combobox(self,width=27,state="readonly")
        self.combo1['values']=self.view_type()
        self.combo1.place(x=10, y=40)
        self.combo1.bind("<<ComboboxSelected>>",self.link)
        self.combo2 = ttk.Combobox(self,width=27,state="readonly")
        self.combo2['values']
        self.combo2.place(x=10, y=70)
        self.combo2.bind("<<ComboboxSelected>>",self.link_showcase)
        self.combo3 = ttk.Combobox(self,width=27,state="readonly")
        self.combo3['values']
        self.combo3.place(x=10, y=100)
        self.combo3.bind("<<ComboboxSelected>>",self.link_shelf)
        self.combo4 = ttk.Combobox(self,width=5,state="readonly")
        self.combo4['values']
        self.combo4.place(x=10, y=130)

        Btn_add=tk.Button(self,text='Добавить',command= lambda:self.add_on_shelf(self.combo4.get()))
        Btn_add.place(x=10,y=160)
        Btn_close=tk.Button(self,text='Закрыть',command=self.destroy)
        Btn_close.place(x=140,y=160)

    def shoes_name(self):
        self.db.cursor.execute('''SELECT name FROM Shoes where id = (%s) ''', (self.id_shoes,))
        return self.db.cursor.fetchone()[0]

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


    def link_shelf(self,select):
        self.name=str(self.combo3.get())
        self.db.cursor.execute('''SELECT id_showcase FROM subdept_showcase where name = (%s) ''', (self.name,))
        self.id_showcase = int(str(self.db.cursor.fetchone()[0]))
        self.combo4.set("")
        self.data=[]
        self.k=0
        self.cal=1
        self.db.cursor.execute('''SELECT id_shelf FROM showcase_shelf where id_showcase = (%s)''', (self.id_showcase,))
        for row in reversed(self.db.cursor.fetchall()):
            self.db.cursor.execute('''SELECT id_shoes FROM shoes_shelf where id_shelf = (%s) and id_shoes is not null''',
        (row[0],))
            for i in self.db.cursor.fetchall():
                self.k=self.k+1
            self.db.cursor.execute('''SELECT kappa FROM shelf where id = (%s)''', (row[0],))
            if self.k!=int(str(self.db.cursor.fetchone()[0])):
                self.data.append(self.cal)
            self.k=0
            self.cal=self.cal+1
        self.combo4['values']=self.data
        return self.cal



    def view_type(self):
        self.db.cursor.execute('''SELECT name FROM departament where id_shop = (%s)''',(self.id_shop,))
        self.data=[]
        for row in self.db.cursor.fetchall():
            if row[0] not in self.data:
                self.data.append(row[0])
        return self.data


    def add_on_shelf(self,level):
        try:
            self.db.cursor.execute('''SELECT id_showcase FROM subdept_showcase where name = (%s)''', (self.combo3.get(),))
            self.id_showcase=int(str(self.db.cursor.fetchone()[0]))

            self.db.cursor.execute('''select showcase_shelf.id_shelf  from showcase
    inner join showcase_shelf ON showcase_shelf.id_showcase  = showcase.id
    inner join shelf ON showcase_shelf.id_shelf  = shelf.id
    where showcase.id = (%s) and shelf.level = (%s)''', (self.id_showcase,level,))
            self.id_shelf=int(str(self.db.cursor.fetchone()[0]))

            # self.db.cursor.execute('''SELECT kappa FROM shelf where id = (%s)''', (self.id_shelf,))

            self.db.cursor.execute('''SELECT id FROM shoes_shelf where id_shelf = (%s) and id_shoes is null''',
            (self.id_shelf,))
            self.id_slot=int(str(self.db.cursor.fetchone()[0]))
            self.db.cursor.execute('''update shoes_shelf set id_shoes = (%s) where id = (%s) ''', (self.id_shoes,self.id_slot,))
            self.db.cursor.execute('''update shoes set count_shelf = count_shelf+1 ,count = count-1 where id = (%s) ''', (self.id_shoes,))
            messagebox.showinfo('Очень важно', 'Товар был поставлен на полку')
            self.b.view_records()
            self.destroy()
        except:
            messagebox.showinfo('Ошибка', 'Выебрите отдел, ветрину и полку')




color=['Хром','Белый','Чёрный','Шоколадный',
'Серый','Тёмно-серый','Зеленный','Тёмно-зелный',
'Синий','Тёмно-синий','Красный','Бордовый',
'Оранжевый','Жёльтый','Бежевый','Розовый','Коричневый','Хаки','Камуфляж']

material=['Натуральная кожа','Искуственная кожа','Резина','Текстиль','ВТМ']


db=Db()
