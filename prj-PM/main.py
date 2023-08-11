import tkinter
import userAction
import productAction


def login():
    global session
    user=txt_user.get()
    pas=txt_pass.get()
    result,access=userAction.user_login(user, pas)
    if result:
        lbl_msg.configure(text="Welcome to your account!",fg="green")
        session=result
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        btn_login.configure(state="disabled")
        for button in buttons:
               if button.cget('text') in access:
                    button.configure(state="active")
    else:
        lbl_msg.configure(text="Wrong username or pass!",fg="red")

def submit():
    def register():
        user=txt_user.get()
        pas=txt_pass.get()
        addr=txt_addr.get()
        result,errorMSG=userAction.user_submit(user, pas, addr)
        if result:
            lbl_msg.configure(text="Submit done",fg="green")
            txt_user.delete(0,"end")
            txt_pass.delete(0,"end")
            txt_addr.delete(0,"end")
            btn_submit.configure(state="disabled")
        else:
            lbl_msg.configure(text=errorMSG,fg="red")
        
    win_submit=tkinter.Toplevel()  
    win_submit.title("Submit panel")
    win_submit.geometry("300x400")
    
    lbl_user=tkinter.Label(win_submit,text="Username: ")
    lbl_user.pack()
    txt_user=tkinter.Entry(win_submit)
    txt_user.pack()

    lbl_pass=tkinter.Label(win_submit,text="Password: ")
    lbl_pass.pack()
    txt_pass=tkinter.Entry(win_submit)
    txt_pass.pack()
    
    lbl_addr=tkinter.Label(win_submit,text="Address: ")
    lbl_addr.pack()
    txt_addr=tkinter.Entry(win_submit)
    txt_addr.pack()
    
    lbl_msg=tkinter.Label(win_submit,text="")
    lbl_msg.pack()
    
    btn_submit=tkinter.Button(win_submit,text="Submit",command=register)
    btn_submit.pack()
    
    
    
    win_submit.mainloop()

def logout():
    global session
    session=False
    btn_admin.configure(state="disabled")
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    btn_shop.configure(state="disabled")
    btn_cart.configure(state="disabled")
    lbl_msg.configure(text="You are logged out now!",fg="green")

def shop():
    def buy():
        global session
        pid=txt_id.get()
        qnt=txt_qnt.get()
        result,msg=productAction.shopValidate(pid, qnt)
        if not result:
            lbl_msg.configure(text=msg,fg="red")
            return
        productAction.saveToCart(session,pid,qnt)
        productAction.updateQnt(pid,qnt)
        lstbx.delete(0,"end")
        products=productAction.getAllProducts()
        for product in products:
            text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
            lstbx.insert("end", text)
        
        lbl_msg.configure(text="Saved to your cart",fg="green")
        txt_id.delete(0,"end")
        txt_qnt.delete(0,"end")
        
    win_shop=tkinter.Toplevel(win)
    win_shop.title("shop panel")
    win_shop.geometry("400x300")
    
    products=productAction.getAllProducts()
    
    
    lstbx=tkinter.Listbox(win_shop,width=60)
    lstbx.pack()
    
    for product in products:
        text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
        lstbx.insert("end", text)
    
    lbl_id=tkinter.Label(win_shop,text="Product id:")
    lbl_id.pack()
    
    txt_id=tkinter.Entry(win_shop)
    txt_id.pack()
    
    lbl_qnt=tkinter.Label(win_shop,text="Quantity:")
    lbl_qnt.pack()
    
    txt_qnt=tkinter.Entry(win_shop)
    txt_qnt.pack()
    
    lbl_msg=tkinter.Label(win_shop,text="")
    lbl_msg.pack()
    
    btn_buy=tkinter.Button(win_shop,text="Buy",command=buy)
    btn_buy.pack()
    
    
    
    win_shop.mainloop()

def mycart():
    global session
    
    win_cart=tkinter.Toplevel(win)
    win_cart.title("cart panel")
    win_cart.geometry("400x300")
    
    lstbx=tkinter.Listbox(win_cart,width=60)
    lstbx.pack()
    
    result=productAction.getUserCart(session)
    for product in result:
        text=f"Name:{product[1]},   Quantity:{product[0]},   Total Price:{product[0]*product[2]}"
        lstbx.insert("end", text)
    
    
    win_cart.mainloop()


def admin():
    def add():
        def insert():
            pname=txt_pname.get()
            price=txt_price.get()
            qnt=txt_qnt.get()
            result,msg=productAction.addNewProduct(pname,price,qnt)
            if not result:
                lbl_msg.configure(text=msg,fg="red")
                return
            lbl_msg.configure(text=msg,fg="green")
                
        

            
        win_add=tkinter.Toplevel(win_admin)
        win_add.title("add new product")
        win_add.geometry("300x300")

        lbl_pname=tkinter.Label(win_add,text="Name")
        lbl_pname.pack()
        txt_pname=tkinter.Entry(win_add)
        txt_pname.pack()

        lbl_price=tkinter.Label(win_add,text="Price")
        lbl_price.pack()
        txt_price=tkinter.Entry(win_add)
        txt_price.pack()

        lbl_qnt=tkinter.Label(win_add,text="Quantity")
        lbl_qnt.pack()
        txt_qnt=tkinter.Entry(win_add)
        txt_qnt.pack()

        lbl_msg=tkinter.Label(win_add,text="")
        lbl_msg.pack()

        btn_add=tkinter.Button(win_add,text="Add",command=insert)
        btn_add.pack()

        

        win_add.mainloop()

    def update():

        def reduction():
            pid=txt_pid.get()
            qnt=txt_qnt.get()
            result,error_msg=productAction.reduceQnt(pid,qnt)
            if result:
                lbl_msg.configure(text="Quantity reduced successfully",fg="green")
                txt_pid.delete(0,"end")
                txt_qnt.delete(0,"end")

                lstbx.delete(0,"end")
                products=productAction.getAllProducts()
                for product in products:
                    text=f"id: {product[0]}     ,Name: {product[1]}    ,Quantity: {product[3]}"
                    lstbx.insert("end",text)
                
            else:
                lbl_msg.configure(text=error_msg,fg="red")

        def addition():
            pid=txt_pid.get()
            qnt=txt_qnt.get()
            result,error_msg=productAction.addQnt(pid,qnt)

            if result:
                lbl_msg.configure(text="Quantity added successfully",fg="green")
                txt_pid.delete(0,"end")
                txt_qnt.delete(0,"end")

                lstbx.delete(0,"end")
                products=productAction.getAllProducts()
                for product in products:
                    text=f"id: {product[0]}     ,Name: {product[1]}    ,Quantity: {product[3]}"
                    lstbx.insert("end",text)
            else:
                lbl_msg.configure(text=error_msg,fg="red") 

        
        win_update=tkinter.Toplevel(win_admin)
        win_update.title("update quantity")
        win_update.geometry("400x350")

        lstbx=tkinter.Listbox(win_update,width=50)
        lstbx.pack()

        products=productAction.getAllProducts()
        for product in products:
            text=f"id: {product[0]}     ,Name: {product[1]}    ,Quantity: {product[3]}"
            lstbx.insert("end",text)
            

        lbl_pid=tkinter.Label(win_update,text="Product id:")
        lbl_pid.pack()
        txt_pid=tkinter.Entry(win_update)
        txt_pid.pack()

        lbl_qnt=tkinter.Label(win_update,text="Quantity:")
        lbl_qnt.pack()
        txt_qnt=tkinter.Entry(win_update)
        txt_qnt.pack()

        btn_reduce=tkinter.Button(win_update,text="-",command=reduction)
        btn_reduce.pack()
        
        btn_add=tkinter.Button(win_update,text="+",command=addition)
        btn_add.pack()

        lbl_msg=tkinter.Label(win_update,text="")
        lbl_msg.pack()
        
        win_update.mainloop()
        

    def grade():
        def determine():
            uid=txt_uid.get()
            grade=txt_grade.get()
            result,msg=userAction.user_setGrade(uid,grade)
            if result :
                lbl_msg.configure(text="Mission completed ",fg="green")
                txt_uid.delete(0,"end")
                txt_grade.delete(0,"end")

                lstbx.delete(0,"end")
                users=userAction.user_info()
                for user in users:
                    text=f"id: {user[0]}   , Name: {user[1]}   , Grade: {user[2]}"
                    lstbx.insert("end",text)
                
            else:
                lbl_msg.configure(text=msg,fg="red")
                
            
            
        win_grade=tkinter.Toplevel(win_admin)
        win_grade.title("users grade")
        win_grade.geometry("300x300")

        lstbx=tkinter.Listbox(win_grade,width=40)
        lstbx.pack()

        users=userAction.user_info()
        for user in users:
            text=f"id: {user[0]}   , Name: {user[1]}   , Grade: {user[2]}"
            lstbx.insert("end",text)
            
 
        lbl_uid=tkinter.Label(win_grade,text="User id:")
        lbl_uid.pack()
        txt_uid=tkinter.Entry(win_grade)
        txt_uid.pack()

        lbl_grade=tkinter.Label(win_grade,text="Grade:")
        lbl_grade.pack()
        txt_grade=tkinter.Entry(win_grade)
        txt_grade.pack()

        lbl_msg=tkinter.Label(win_grade,text="")
        lbl_msg.pack()

        btn_grade=tkinter.Button(win_grade,text="ok",command=determine)
        btn_grade.pack()

        win_grade.mainloop()
    
    win_admin=tkinter.Toplevel(win)
    win_admin.title("admin panel")
    win_admin.geometry("300x150")

    btn_newp=tkinter.Button(win_admin,text="New product",command=add)
    btn_newp.pack()

    btn_update=tkinter.Button(win_admin,text="Update quantity",command=update)
    btn_update.pack()

    btn_level=tkinter.Button(win_admin,text="Access level",command=grade)
    btn_level.pack()
    

    win_admin.mainloop()
# ------------------ Main ---------------------------

session=False

win=tkinter.Tk()
win.title("SHOP PROJECT")
win.geometry("300x300")

lbl_user=tkinter.Label(win,text="Username: ")
lbl_user.pack()
txt_user=tkinter.Entry(win)
txt_user.pack()

lbl_pass=tkinter.Label(win,text="Password: ")
lbl_pass.pack()
txt_pass=tkinter.Entry(win)
txt_pass.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()

btn_login=tkinter.Button(win,text="Login",command=login)
btn_login.pack()

btn_submit=tkinter.Button(win,text="Submit",command=submit)
btn_submit.pack()

btn_logout=tkinter.Button(win,text="Logout",state="disabled", command=logout)
btn_logout.pack()

btn_shop=tkinter.Button(win,text="Shop",state="disabled", command=shop)
btn_shop.pack()

btn_cart=tkinter.Button(win,text="My cart",state="disabled", command=mycart)
btn_cart.pack()


btn_admin=tkinter.Button(win,text="Admin",state="disabled",command=admin)
btn_admin.pack()

buttons=[btn_submit,btn_admin,btn_shop,btn_cart,btn_logout]



win.mainloop()



