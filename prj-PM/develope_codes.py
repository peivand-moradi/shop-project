import sqlite3
cnt=sqlite3.connect('store.db')
# --------- create products table----------------
# sql='''CREATE TABLE products 
#     (id INTEGER PRIMARY KEY ,
#      pname CHAR(30) NOT NULL,
#      price INTEGER NOT NULL,
#      qnt INTEGER NOT NULL)'''
# cnt.execute(sql)

# ------------- insert new products -------------

# sql=''' INSERT INTO products(pname,price,qnt)
#         VALUES('acer laptop 12000',700,6)'''
# cnt.execute(sql)
# cnt.commit()

# --------- create cart table----------------
##sql='''CREATE TABLE cart 
##    (id INTEGER PRIMARY KEY ,
##      uid INTEGER NOT NULL,
##      pid INTEGER NOT NULL,
##      qnt INTEGER NOT NULL)'''
##cnt.execute(sql)







        
