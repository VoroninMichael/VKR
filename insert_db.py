import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                          password="1234",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="shop")
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

    def insert_data(self,name,sh_type,color,material,count,b_data,price,discount
    # vendor
    ):
        self.cursor.execute ('''INSERT INTO shoes(name,sh_type,color,material,count,b_data,price,discount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ''',
                            (name,sh_type,color,material,count,b_data,price,discount))
        self.connection.commit()

    def insert_vendor(self,vendor):
        self.cursor.execute ('''INSERT INTO vendor (name) VALUES (%s) ''',
                            (vendor,))
        self.connection.commit()

    def insert_shop(self,address,countmax):
        self.cursor.execute('''INSERT INTO shop (address,countmax) VALUES (%s,%s)''',
                            (address,countmax,))
        self.connection.commit()
        self.cursor.execute('''SELECT  id FROM shop where address = (%s) ''',
                                                                    (address,))
        self.id_shop=self.cursor.fetchone()
        self.cursor.execute('''INSERT INTO warehouse(id_shop) VALUES (%s)''',
                                                        (self.id_shop))

        self.connection.commit()

    def insert_employe(self,name,login,password,admin,address):
        self.cursor.execute('''SELECT  id FROM shop where address = (%s) ''',
                                                                    (address,))
        self.id_shop=self.cursor.fetchone()
        self.cursor.execute('''INSERT INTO employees (name,login,pass,admin,id_shop) VALUES (%s,%s,%s,%s,%s)''',
                            (name,login,password,bool(admin),self.id_shop))



    def insert_type(self,name):
        self.cursor.execute('''INSERT INTO dept (name) VALUES (%s)''',
                            (name,))
        self.connection.commit()


    def insert_subtype(self,typename,subtypename,sex):
            self.cursor.execute ('''INSERT INTO subdept (name) VALUES (%s) ''',
                                (subtypename,))
            self.connection.commit()

            self.cursor.execute('''SELECT id from subdept where name = (%s)''',(subtypename,))
            self.id_subtype=self.cursor.fetchone()
            self.connection.commit()

            self.cursor.execute('''SELECT id from dept where name = (%s)''',(typename,))
            self.id_type=self.cursor.fetchone()
            self.connection.commit()

            self.cursor.execute ('''INSERT INTO dept_subdept(id_dept,id_subdept,sex) VALUES (%s,%s,%s) ''',
                                (self.id_type,self.id_subtype,sex))
            self.connection.commit()



    def insert_showcase(self,name,levelmax,kappa):
        self.cursor.execute (''' INSERT INTO showcase(name,levelmax) VALUES (%s,%s)''',
                                                                                (name,levelmax))

        self.cursor.execute('''SELECT id FROM showcase where name = (%s)''', (name,))
        self.id_showcase=int(str(self.cursor.fetchone()[0]))




        row=1
        while int(row) <= int(levelmax):
            self.cursor.execute(''' INSERT INTO shelf(level,kappa) VALUES (%s,%s)''',
                                                                                (str(row),kappa))

            row=row+1



        self.cursor.execute(''' SELECT max(id) from shelf''')
        self.max_id_shelf= int(str(self.cursor.fetchone()[0]))


        while int(levelmax) >  0 :
            self.cursor.execute(''' INSERT INTO showcase_shelf(id_showcase,id_shelf) VALUES (%s,%s)''',
                                                                                (self.id_showcase,self.max_id_shelf))
            int(self.max_id_shelf)
            for i in range(int(kappa)):
                self.cursor.execute(''' INSERT INTO shoes_shelf(id_shelf) VALUES (%s)''',
                                                                                    (self.max_id_shelf,))
            self.max_id_shelf=self.max_id_shelf-1

            int(levelmax)
            levelmax=int(levelmax)-1


    def insert_shelf(self,name,kappa):

        self.cursor.execute('''SELECT id FROM showcase where name = (%s)''', (name,))
        self.id_showcase=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()

        self.cursor.execute('''SELECT levelmax FROM showcase where name = (%s)''', (name,))
        self.maxlevel=int(str(self.cursor.fetchone()[0]))+1
        self.connection.commit()
        self.cursor.execute(''' UPDATE showcase SET levelmax = (%s) where name = (%s)''',
                                                                            (self.maxlevel,name))
        self.cursor.execute(''' INSERT INTO shelf (level,kappa) VALUES (%s,%s)''',
                                                                            (self.maxlevel,kappa))

        self.cursor.execute(''' SELECT max(id) from shelf''')
        self.id_shelf=self.cursor.fetchone()
        self.connection.commit()
        self.cursor.execute(''' INSERT INTO showcase_shelf(id_showcase,id_shelf) VALUES (%s,%s)''',
                                                                                (self.id_showcase,self.id_shelf))
        for i in range(int(kappa)):
            self.cursor.execute(''' INSERT INTO shoes_shelf(id_shelf) VALUES (%s)''',
                                                                                (self.id_shelf,))

    def inserttypeshowcase(self,nameshowcase,namesubtype):
        self.cursor.execute('''SELECT id FROM showcase where name = (%s)''', (nameshowcase,))
        self.id_showcase=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()
        self.cursor.execute('''SELECT id FROM subdept where name = (%s)''', (namesubtype,))
        self.id_subtype=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()
        self.name=str(str(self.id_showcase)+" "+nameshowcase+" "+ namesubtype )
        self.cursor.execute(''' INSERT INTO subdept_showcase(id_subdept,id_showcase,name) VALUES (%s,%s,%s)''',
                                                                                (self.id_subtype,self.id_showcase,self.name,))



    def insert_subdepartament(self,name,name_showcase,sex):
        self.cursor.execute('''SELECT id FROM subdept_showcase where name = (%s)''', (name_showcase,))
        self.id_subdept_showcase=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()
        self.name = str(str(self.id_subdept_showcase)+" "+name)
        self.cursor.execute(''' INSERT INTO depttype (name,id_subdept,sex) VALUES (%s,%s,%s)''',
                                                    (self.name,self.id_subdept_showcase,sex))


    def update_departament(self,shop,name,subname):
        self.cursor.execute('''SELECT id FROM shop where address = (%s)''', (shop,))
        self.id_shop=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()
        self.name = str(str(self.id_shop)+" "+name)
        self.cursor.execute('''SELECT id FROM depttype where name = (%s)''', (subname,))
        for row in self.cursor.fetchall():
            self.cursor.execute(''' INSERT INTO departament (name,id_shop,id_depttype) VALUES (%s,%s,%s)''',
                                                        (self.name,self.id_shop,row[0]))



    def update_departament(self,namedep,namesubdep):
        self.cursor.execute('''SELECT id_shop FROM departament where name = (%s)''', (namedep,))
        self.id_shop=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()
        self.cursor.execute('''SELECT id FROM depttype where name = (%s)''', (namesubdep,))
        self.id_depttype=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()
        self.cursor.execute(''' INSERT INTO departament (name,id_shop,id_depttype) VALUES (%s,%s,%s)''',
                                                    (namedep,self.id_shop,self.id_depttype))



    def insert_shoes(self,name,subtype,color,material,season,size,vendor,d_vendor,price,discount,count,id_shop):
        self.cursor.execute('''INSERT INTO shoes(name,sh_type,material,season,price,discount,count) VALUES (%s,%s,%s,%s,%s,%s,%s)''',
                                                (name,subtype,material,season,price,discount,count,))
        self.cursor.execute('''SELECT id FROM shoes where name = (%s)''', (name,))
        self.id_shoes=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()

        self.cursor.execute('''SELECT id FROM warehouse where id_shop = (%s)''', (id_shop,))
        self.id_warehouse=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()

        self.cursor.execute('''SELECT id FROM vendor where name = (%s)''', (vendor,))
        self.id_vendor=int(str(self.cursor.fetchone()[0]))
        self.connection.commit()

        self.cursor.execute('''INSERT INTO color(color,id_shoes) VALUES (%s,%s)''',
                                                (color,self.id_shoes,))
        self.connection.commit()

        self.cursor.execute('''INSERT INTO size(size,id_shoes) VALUES (%s,%s)''',
                                                (size,self.id_shoes,))
        self.connection.commit()

        self.cursor.execute('''INSERT INTO vendor_shoes(id_vendor,id_shoes,de_date) VALUES (%s,%s,%s)''',
                                                (self.id_vendor,self.id_shoes,d_vendor,))
        self.connection.commit()

        self.cursor.execute('''INSERT INTO warehouse_shoes (id_warehouse,id_shoes) VALUES (%s,%s)''',
                                                (self.id_warehouse,self.id_shoes))
        self.connection.commit()
