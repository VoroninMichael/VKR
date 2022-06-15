import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import Calendar,DateEntry

from insert_db import Db



class New(tk.Toplevel):
    def __init__(self,window,id_shop,departament,subdept,showcase,brand,color,season,st1,st2):
        super().__init__()
        self.db=db
        self.id_shop= id_shop
        self.dept=departament
        self.subdept=subdept
        self.showcase=showcase

        self.brand=brand
        self.color=color
        self.season=season
        self.st1 =bool(st1)
        self.st2 =bool(st2)
        self.view=window

        self.open_dialog()

    def open_dialog(self):
        self.title("Merchendaiser")
        self.geometry('583x267')
        self.resizable(False,False)
        self.grab_set()
        self.focus_set()
        self.tree= ttk.Treeview(self,columns=('ID','name','type','vendor','color','material','season','price','discount'),height=10,  show='headings')


        self.tree.column('ID', width=20, anchor=tk.CENTER)
        self.tree.column('name', width=90, anchor=tk.CENTER)
        self.tree.column('type', width=90, anchor=tk.CENTER)
        self.tree.column('color', width=60, anchor=tk.CENTER)
        self.tree.column('material', width=70, anchor=tk.CENTER)
        self.tree.column('vendor', width=80, anchor=tk.CENTER)
        self.tree.column('season', width=50, anchor=tk.CENTER)
        self.tree.column('price', width=52, anchor=tk.CENTER)
        self.tree.column('discount', width=50, anchor=tk.CENTER)


        self.tree.heading('ID',text='id')
        self.tree.heading('name',text='Название')
        self.tree.heading('type',text='Подвид')
        self.tree.heading('color',text='Цвет')
        self.tree.heading('material',text='Матерьял')
        self.tree.heading('vendor',text='Поставщик')
        self.tree.heading('season',text='Сезон')
        self.tree.heading('price',text='Цена')
        self.tree.heading('discount',text='Скидка')
        self.ysb = ttk.Scrollbar(self, command=self.tree.yview)
        self.tree.configure(yscroll=self.ysb.set)
        self.ysb.pack(side=tk.RIGHT,fill="y")
        self.tree.place(x=1,y=1)
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.auto_asuslegen()

        btn_add=ttk.Button(self,text="Принять выкладку",command=self.add_on_shelf)

        btn_add.place(x=1,y=230)
        btn_update=ttk.Button(self,text="Убрать товар",command=self.write_off)
        btn_update.place(x=120,y=230)
        btn_delete=ttk.Button(self,text="Отказаться от выкладки",command=self.destroy)
        btn_delete.place(x=210,y=230)

    def auto_asuslegen(self):
        self.free=[]
        self.space=[]
        self.free_shelf(self.free,self.space)
        a1=False
        a2=False
        a3=False
        if self.brand != "Бренды":
            a1=True
        if self.color != "Цвета":
            a2=True
        if self.season != "Сезоны":
            a3=True
        self.find_id()


        if self.st1 ==True and self.st2 ==True and a1==True and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==True and a1==True and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+self.type_showcase+"'"+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==True and a1==True and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==True and a1==False and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"

            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==True and a1==True and a2==False and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+self.type_showcase+"'"+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"

            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==True and a1==False and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and c.color='+"'"+self.color+"'"

            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==True and a1==False and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and shoes.season='+"'"+self.season+"'"

            self.find_shoes(b)

        if self.st1 ==False and self.st2 ==True and a1==True and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 '+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"

            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==True and a1==True and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 '+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==True and a1==True and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 '+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==True and a1==False and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 '+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+"'"+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==True and a1==True and a2==False and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 '+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and v.name='+"'"+self.brand+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==True and a1==False and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 '+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and c.color='+"'"+self.color+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==True and a1==False and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 '+' and dept_subdept.sex='+"'"+self.sex_subdept+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)

        if self.st1 ==True and self.st2 ==False and a1==True and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==False and a1==True and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==False and a1==True and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and v.name='+"'"+self.brand+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==False and a1==False and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==False and a1==True and a2==False and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and v.name='+"'"+str(self.brand)+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==False and a1==False and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and c.color='+"'"+self.color+"'"
            self.find_shoes(b)
        if self.st1 ==True and self.st2 ==False and a1==False and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.sh_type='+"'"+str(self.type_showcase)+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)


        if self.st1 ==False and self.st2 ==False and a1==True and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0'+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==False and a1==True and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0'+' and v.name='+"'"+self.brand+"'"+' and c.color='+"'"+self.color+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==False and a1==True and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0'+' and v.name='+"'"+self.brand+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==False and a1==False and a2==True and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0'+' and c.color='+"'"+self.color+"'"+' and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==False and a1==True and a2==False and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0'+' and v.name='+"'"+self.brand+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==False and a1==False and a2==True and a3 == False:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0'+' and c.color='+"'"+self.color+"'"
            self.find_shoes(b)
        if self.st1 ==False and self.st2 ==False and a1==False and a2==False and a3 == True:
            b='shop.id='+str(self.id_shop)+'and shoes.count>0 and shoes.season='+"'"+self.season+"'"
            self.find_shoes(b)
            self.preview()

    def find_id(self):
        self.db.cursor.execute('''SELECT id FROM departament where id_shop = (%s) and name=(%s)''',(self.id_shop,self.dept,))
        self.id_departament=int(str(self.db.cursor.fetchone()[0]))
        self.db.cursor.execute('''SELECT id FROM depttype where name=(%s)''',(self.subdept,))
        self.id_subdept=int(str(self.db.cursor.fetchone()[0]))
        self.db.cursor.execute('''SELECT id_showcase FROM subdept_showcase where name = (%s)''', (self.showcase,))
        self.id_showcase=int(str(self.db.cursor.fetchone()[0]))
        self.db.cursor.execute('''SELECT subdept.name FROM subdept_showcase
inner join subdept on subdept_showcase.id_subdept = subdept.id where subdept_showcase.id_showcase=(%s) ''', (self.id_showcase,))
        self.type_showcase=str(self.db.cursor.fetchone()[0])
        self.db.cursor.execute('''select sex from depttype where id = (%s)''',(self.id_subdept,))
        self.sex_subdept=str(self.db.cursor.fetchone()[0])

    def free_shelf(self,free,space):
        self.db.cursor.execute('''SELECT id_showcase FROM subdept_showcase where name = (%s)''', (self.showcase,))
        self.id_showcase=int(str(self.db.cursor.fetchone()[0]))
        self.db.cursor.execute('''SELECT levelmax FROM showcase where id = (%s)''', (self.id_showcase,))
        self.levelmax=int(str(self.db.cursor.fetchone()[0]))
        for i in range(self.levelmax):
            self.data=[]
            self.db.cursor.execute('''SELECT id_shelf FROM showcase_shelf where id_showcase = (%s)''', (self.id_showcase,))
            for row in reversed(self.db.cursor.fetchall()):
                self.data.append(row[0])
            self.db.cursor.execute('''SELECT count(*)  from shoes_shelf
    inner join shoes  ON shoes_shelf.id_shoes  = shoes.id
    inner join color on shoes.id=color.id_shoes where shoes_shelf.id_shelf= (%s) and shoes_shelf.id_shoes is not null ''', (self.data[i],))
            occupied=(int(str(self.db.cursor.fetchone()[0])))
            self.db.cursor.execute('''SELECT kappa FROM shelf where id = (%s)''', (self.data[i],))
            free.append((int(str(self.db.cursor.fetchone()[0]))-occupied))
            space.append(self.data[i])
        return free,space

    def find_shoes(self,x):
        self.data_shoes=[]
        self.db.cursor.execute('''select DISTINCT shoes.id  from shoes
inner join color  c  ON c.id_shoes  = shoes.id
inner join  vendor_shoes  vs on vs.id_shoes = shoes.id
inner join vendor v  on v.id = vs.id_vendor
inner join warehouse_shoes on warehouse_shoes.id_shoes =shoes.id
inner join warehouse on warehouse.id = warehouse_shoes.id_warehouse
inner join shop on shop.id = warehouse.id_shop
inner join departament on departament.id_shop=shop.id
inner join depttype on depttype.id= departament.id_depttype
inner join subdept_showcase on subdept_showcase.id = depttype.id_subdept
inner join subdept on subdept.id = subdept_showcase.id_subdept
inner join dept_subdept on dept_subdept.id_subdept = subdept.id
where %s'''% x)
        for row in self.db.cursor.fetchall():
            self.data_shoes.append(row[(0)])
        if len(self.data_shoes)>0:
            if len(self.data_shoes)<len(self.free):
                messagebox.showinfo('Очень важно', 'Товара не достаточно, чтоб заполнить им всю ветрину')
                self.preview()
            else:
                self.preview()
        else:
            messagebox.showinfo('Очень важно', 'Нет товара, удовлетворяющий запрос')
            self.destroy()


        self.data_shoes_remove=[]
        for i in range(self.levelmax):
            self.data=[]
            self.db.cursor.execute('''SELECT id_shelf FROM showcase_shelf where id_showcase = (%s)''', (self.id_showcase,))
            for row in reversed(self.db.cursor.fetchall()):
                self.data.append(row[0])
            self.db.cursor.execute('''SELECT count(*)  from shoes_shelf
inner join shoes  ON shoes_shelf.id_shoes  = shoes.id
inner join color on shoes.id=color.id_shoes where shoes_shelf.id_shelf= (%s) and shoes_shelf.id_shoes is not null ''', (self.data[i],))
            self.occupied=int(str(self.db.cursor.fetchone()[0]))
            self.db.cursor.execute('''SELECT id_shoes FROM shoes_shelf where id_shelf = (%s)''', (self.data[i],))
            for j in range(self.occupied):
                self.db.cursor.execute('''select shoes.id from shoes_shelf
                inner join shoes  ON shoes_shelf.id_shoes  = shoes.id
                where shoes_shelf.id_shelf = (%s)
                ''', (self.data[i],))
                self.data_shoes_remove.append(self.db.cursor.fetchone()[0])
        for i in self.data_shoes_remove:
            for j in self.data_shoes:
                if i == j:
                    self.data_shoes.remove(i)
                else:
                    continue




    def preview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        k=0
        a=0
        lensh=len(self.data_shoes)
        for row in self.free:
            self.db.cursor.execute('''select level from shelf where id= (%s)''',(self.space[a],))
            self.tree.insert('', tk.END, values=(int(str(self.db.cursor.fetchone()[0]))," Полка"))
            a=a+1

            rowrange=row

            if lensh <= 0:
                k=0
                break
            else:
                if row > len(self.data_shoes):
                    rowrange=rowrange-(row-len(self.data_shoes))
            for i in range(rowrange):
                self.db.cursor.execute(''' select  DISTINCT shoes.id,  shoes.name,shoes.sh_type,v.name, c.color, shoes.material, shoes.season,shoes.price,shoes.discount from shoes
            inner join color  c  ON c.id_shoes  = shoes.id
            inner join size  s on s.id_shoes = shoes.id
            inner join  vendor_shoes  vs on vs.id_shoes = shoes.id
            inner join vendor v  on v.id = vs.id_vendor
            inner join warehouse_shoes on warehouse_shoes.id_shoes =shoes.id
            inner join warehouse on warehouse.id = warehouse_shoes.id_warehouse
            inner join shop on shop.id = warehouse.id_shop
            where  shoes.id=(%s)
            ''',(self.data_shoes[k],))
                [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]
                k=k+1
                lensh=lensh-1





    def add_on_shelf(self):
        k=0
        a=-1
        lensh=len(self.data_shoes)
        for row in self.free:
            a=a+1
            rowrange=row
            if lensh <= 0:
                k=0
                break
            else:
                if row > len(self.data_shoes):
                    rowrange=rowrange-(row-len(self.data_shoes))
            for i in range(rowrange):
                self.db.cursor.execute('''SELECT id FROM shoes_shelf where id_shelf = (%s) and id_shoes is null''',
                (self.space[a],))
                self.id_slot=int(str(self.db.cursor.fetchone()[0]))
                self.db.cursor.execute('''update shoes_shelf set id_shoes = (%s) where id = (%s) ''', (self.data_shoes[k],self.id_slot,))
                self.db.cursor.execute('''update shoes set count_shelf = count_shelf+1 ,count = count-1 where id = (%s) ''', (self.data_shoes[k],))
                k=k+1
        messagebox.showinfo('Очень важно', 'Товар был поставлен на полки')
        self.destroy()

    def write_off(self):
        try:
            self.data_shoes.remove(int(self.tree.set(self.tree.selection()[0],'#1')))
            for i in self.tree.get_children():
                self.tree.delete(i)
            messagebox.showinfo('Очень важно', 'Товар был заменен или убран')
            self.preview()
        except:
            messagebox.showinfo('Ошибка', 'Выберите товар, который хотите убрать')

color=['Хром','Белый','Чёрный','Шоколадный',
'Серый','Тёмно-серый','Зеленный','Тёмно-зелный',
'Синий','Тёмно-синий','Красный','Бордовый',
'Оранжевый','Жёльтый','Бежевый','Розовый','Коричневый','Хаки','Камуфляж']
db=Db()
