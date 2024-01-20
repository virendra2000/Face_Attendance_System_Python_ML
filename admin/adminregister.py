from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from cryptography.fernet import Fernet
import mysql.connector as mysql
key = Fernet.generate_key()
fernet = Fernet(key)
def adminregisterpage():
    #configuring window
    adminregister = Tk()
    adminregister.title("Admin Register")
    adminregister.geometry("1920x1080")
    adminregister.configure(bg='#010c20')

    icoimg = PhotoImage(file="favicon.png",master=adminregister)
    icolabel = Label(adminregister,image=icoimg,bg="#010c20")
    icolabel.image = icoimg
    icolabel.place(x=650,y=20)

    label1 = Label(adminregister, text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 bold'))
    label1.place(x=400,y=150)
    label1.config(bg = "#010c20",fg= "white")

    #mainlabel
    titlelabel = Label(adminregister, text='ADMIN REGISTER',font= ('Helvetica 20 italic bold'))
    titlelabel.place(x=600,y=250)
    titlelabel.config(bg = "#010c20",fg= "white")


    #adminnamelabel
    adminnamelabel = Label(adminregister, text='Admin Name',font= ('Helvetica 14 italic bold'))
    adminnamelabel.pack()
    adminnamelabel.place(x=600,y=300)
    adminnamelabel.config(bg = "#010c20",fg="white")


    #adminnametxt
    adminnametxt = Entry(adminregister,font=('calibre',14,'normal'))
    adminnametxt.pack()
    adminnametxt.place(x=600,y=350)


    #adminusernamelabel
    usernamelabel = Label(adminregister, text='Username',font= ('Helvetica 14 italic bold'))
    usernamelabel.pack()
    usernamelabel.place(x=600,y=400)
    usernamelabel.config(bg = "#010c20",fg="white")


    #adminusernametxt
    usernametxt = Entry(adminregister,font=('calibre',14,'normal'))
    usernametxt.pack()
    usernametxt.place(x=600,y=450)


    #passwordlabel
    passwordlabel = Label(adminregister, text='Password',font= ('Helvetica 14 italic bold'))
    passwordlabel.pack()
    passwordlabel.place(x=600,y=500)
    passwordlabel.config(bg = "#010c20",fg="white")

    #password text entry
    passwordtxt = Entry(adminregister,show="*",font=('calibre',14,'normal'))
    passwordtxt.pack()
    passwordtxt.place(x=600,y=550)

    def submit():
        adminname = adminnametxt.get()
        username = usernametxt.get()
        password = passwordtxt.get()
        passw = fernet.encrypt(password.encode())
        mydb = mysql.connect(
            host = "localhost",
            user = "root",
            password = "Rootadmin@2023",
            database = "sysattendence"
        )
        c = mydb.cursor()
        sql = "INSERT INTO administrator(name,username,password) VALUES(%s,%s,%s)"
        val = (adminname,username,passw)
        c.execute(sql,val)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Registration Message", "Successfully Submitted")
        
    regimg = PhotoImage(file="register.png",master=adminregister)
    #Register Button
    registerbtn = Button(adminregister,image=regimg, text = "Register",font= ('Helvetica 12 bold'),highlightthickness=0,borderwidth=0,bg='#010c20',fg='blue',command=submit)
    registerbtn.image = regimg
    registerbtn.place(x=620,y=600)
