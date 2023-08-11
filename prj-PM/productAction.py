import sqlite3
cnt=sqlite3.connect('store.db')

def getAllProducts():
    sql='''SELECT * FROM products'''
    result=cnt.execute(sql)
    rows=result.fetchall()
    return rows

def shopValidate(pid,qnt):
    if pid=="" or qnt=="":
        return False,"Fill the inputs"
    
    sql='''SELECT * FROM PRODUCTS WHERE id=?'''
    result=cnt.execute(sql,(pid,))
    rows=result.fetchone()
    if not rows:
        return False,"Wrong product id"
    
    sql='''SELECT * FROM PRODUCTS WHERE id=? AND qnt>=?'''
    result=cnt.execute(sql,(pid,qnt))
    rows=result.fetchone()
    if not rows:
        return False,"Not enough quantity"
    
    return True,""

def saveToCart(uid,pid,qnt):
    sql=''' INSERT INTO cart(uid,pid,qnt) VALUES(?,?,?)'''
    cnt.execute(sql,(uid,pid,qnt))
    cnt.commit()

def updateQnt(pid,qnt):
    sql=''' UPDATE products SET qnt=qnt-? WHERE id=?'''
    cnt.execute(sql,(qnt,pid))
    cnt.commit()

def getUserCart(uid):
    sql=''' SELECT cart.qnt,products.pname,products.price
            FROM cart INNER JOIN products ON
            cart.pid=products.id
            WHERE cart.uid=?'''
    result=cnt.execute(sql,(uid,))
    rows=result.fetchall()
    return rows
    
def productValidate(pname,price,qnt):
    if pname=="" or price=="" or qnt=="":
        return False,"Fill the inputs"
    sql='''SELECT * FROM products WHERE pname=?'''
    result=cnt.execute(sql,(pname,))
    rows=result.fetchone()

    if rows:
        return False,"This product already exist"

    return True,""
    
def addNewProduct(pname,price,qnt):
    result,errorMsg=productValidate(pname,price,qnt)
    if result:
        sql='''INSERT INTO products (pname,price,qnt) VALUES(?,?,?)'''
        cnt.execute(sql,(pname,price,qnt))
        cnt.commit()
        return True,"Product is added successfully"
    else:
        return False,errorMsg
    
    
    
def quantityValidate(pid,qnt):
    if pid=="" or qnt=="":
        return False,"fill the blanks"
    sql='''SELECT * FROM products WHERE id=?'''
    result=cnt.execute(sql,(pid,))
    rows=result.fetchone()

    if not rows:
        return False,"Wrong product id"
    return True,""


def reduceQnt(pid,qnt):
    result,msg=quantityValidate(pid,qnt)
    if result:
        sql='''UPDATE products SET qnt=qnt-? WHERE id=?'''
        cnt.execute(sql,(qnt,pid))
        cnt.commit()
        return True ,""
    else:
        return False,msg

def addQnt(pid,qnt):
    result,msg=quantityValidate(pid,qnt)
    if result:
        sql='''UPDATE products SET qnt=qnt+? WHERE id=?'''
        cnt.execute(sql,(qnt,pid))
        cnt.commit()
        return True ,""
    else:
        return False,msg
    
    
    
    
    
    
    
    
