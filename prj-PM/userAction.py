import sqlite3
import json

cnt=sqlite3.connect("store.db")

def user_login(user,pas):
    global cnt
    sql=''' SELECT * FROM users WHERE username=? AND pass=?'''
    result=cnt.execute(sql,(user,pas))
    row=result.fetchone()
    
    if row:
        return row[0],loadGrade(row[4])
    else:
        return False,""

def validation(user,pas,addr):
    global cnt
    if user=="" or pas=="" or addr=="":
        return False,"Fill the empty fields"
    if len(pas)<8:
        return False,"Password length error"
    
    sql=''' SELECT * FROM users WHERE username=?'''
    result=cnt.execute(sql,(user,))
    row=result.fetchone()
    if row:
        return False,"Username already exist!"
    
    return True,""
    
    
    
def user_submit(user,pas,addr):
    global cnt
    result,errorMSG=validation(user,pas,addr)
    if result:
        sql='''INSERT INTO users (username,pass,addr,grade)
                VALUES(?,?,?,?)'''
        cnt.execute(sql,(user,pas,addr,2))
        cnt.commit()
        return True,""
    else:
        return False,errorMSG
    

def user_info():
    sql='''SELECT id,username,grade FROM users '''
    result=cnt.execute(sql)
    row=result.fetchall()
    return row


def gradeValidation(uid,grade):
    if uid=="" or grade=="":
        return False,"fill the blanks"
    sql='''SELECT * FROM users WHERE id=?'''
    result=cnt.execute(sql,(uid,))
    row=result.fetchone()
    if not row:
        return False,"Wrong user id"
    return True,""



def user_setGrade(uid,grade):
    result,errorMsg=gradeValidation(uid,grade)
    if result:
        sql='''UPDATE users SET grade=? WHERE id=?'''
        cnt.execute(sql,(grade,uid))
        cnt.commit()
        return True,""
    else:
        return False,errorMsg

def loadGrade(grade):
    with open("setting.json")as f:
        content=json.load(f)
    return content[str(grade)]    
    
 
    
