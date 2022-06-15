import tkinter as tk
from tkinter import ttk,messagebox
from insert_db import Db
# from tkcalendar import Calendar,DateEntry

class Shoes_all(tk.Toplevel):
    def __init__(self,window):
        super().__init__(window)
        self.db=db
        self.window=window
        self.open_dialog()

    def open_dialog(self):
        self.title("Merchendaiser - AllShops")
        self.geometry('720x350')
        self.resizable(False,False)

        self.text1 = ttk.Entry(self,width=55)
        self.text1.place(x=1,y=3)
        btn_search=ttk.Button(self,text="Поиск",command= lambda:self.search(self.text1.get()))
        btn_search.pack(fill="y")
        btn_view=ttk.Button(self,text="Показать всё",command= self.view_records)
        btn_view.place(x=430,y=1)

        self.tree= ttk.Treeview(self,columns=('adress','ID','name','sh_type','count','color','material','season','size','vendor','d_data','discount','price'),height=15,  show='headings')
        self.tree.column('adress', width=80, anchor=tk.CENTER)
        self.tree.column('ID', width=20, anchor=tk.CENTER)
        self.tree.column('name', width=80, anchor=tk.CENTER)
        self.tree.column('sh_type', width=90, anchor=tk.CENTER)
        self.tree.column('count', width=60, anchor=tk.CENTER)
        self.tree.column('color', width=80, anchor=tk.CENTER)
        self.tree.column('material', width=80, anchor=tk.CENTER)
        self.tree.column('season', width=80, anchor=tk.CENTER)
        self.tree.column('size', width=60, anchor=tk.CENTER)
        self.tree.column('vendor', width=80, anchor=tk.CENTER)
        self.tree.column('d_data', width=50, anchor=tk.CENTER)
        self.tree.column('discount', width=60, anchor=tk.CENTER)
        self.tree.column('price', width=50, anchor=tk.CENTER)

        self.tree.heading('adress',text='Адрес')
        self.tree.heading('ID',text='ID')
        self.tree.heading('name',text='Название')
        self.tree.heading('sh_type',text='Тип обуви')
        self.tree.heading('count',text='Кол-во')
        self.tree.heading('color',text='цвет')
        self.tree.heading('material',text='Матерьял')
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
        self.view_records()

    def view_records(self):
        self.db.cursor.execute('''select shop.address,shoes.id ,shoes.name,shoes.sh_type,shoes.count, c.color, shoes.material, s.size, v.name as vendor, vs.de_date,shoes.discount,shoes.price from shoes
    inner join color  c  ON c.id_shoes  = shoes.id
    inner join size  s on s.id_shoes = shoes.id
    inner join  vendor_shoes  vs on vs.id_shoes = shoes.id
    inner join vendor v  on v.id = vs.id_vendor
    inner join warehouse_shoes on warehouse_shoes.id_shoes =shoes.id
    inner join warehouse on warehouse.id = warehouse_shoes.id_warehouse
    inner join shop on shop.id = warehouse.id_shop
    where  shoes.status=False and shoes.count != 0
                                ''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]


    def search(self,search):
        self.db.cursor.execute('''select shop.address,shoes.id ,shoes.name,shoes.sh_type,shoes.count, c.color, shoes.material, s.size, v.name as vendor, vs.de_date,shoes.discount,shoes.price from shoes
inner join color  c  ON c.id_shoes  = shoes.id
inner join size  s on s.id_shoes = shoes.id
inner join  vendor_shoes  vs on vs.id_shoes = shoes.id
inner join vendor v  on v.id = vs.id_vendor
inner join warehouse_shoes on warehouse_shoes.id_shoes =shoes.id
inner join warehouse on warehouse.id = warehouse_shoes.id_warehouse
inner join shop on shop.id = warehouse.id_shop
where shoes.status=False and shoes.count != 0 and shoes.name LIKE %s
                                ''',(search,))
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]

db=Db()
