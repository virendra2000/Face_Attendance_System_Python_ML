from tkinter import *
from PIL import ImageTk,Image
import admin.adminregister as areg
import admin.admindashboard as amenu
import admin.logindata as b1
from tkinter import messagebox
import mysql.connector as mysql
from tkinter.filedialog import (askopenfilename, asksaveasfilename)
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
def adminloginpage():
    adminlogin = Tk()
    adminlogin.title("Admin Login")
    adminlogin.geometry("1920x1080")
    adminlogin.configure(bg='#010c20')

    icoimg = PhotoImage(file="favicon.png",master=adminlogin)
    icolabel = Label(adminlogin,image=icoimg,bg="#010c20")
    icolabel.place(x=650,y=20)

    label1 = Label(adminlogin, text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 bold'))
    label1.place(x=400,y=150)
    label1.config(bg = "#010c20",fg= "white")

    #mainlabel
    titlelabel = Label(adminlogin, text='ADMIN LOGIN',font= ('Helvetica 20 bold'))
    titlelabel.place(x=600,y=250)
    titlelabel.config(bg = "#010c20",fg= "white")

    #usernamelabel
    usernamelabel = Label(adminlogin, text='Username',font= ('Helvetica 14 bold'))
    usernamelabel.pack()
    usernamelabel.place(x=600,y=300)
    usernamelabel.config(bg = "#010c20",fg="white")

    #usernametxt
    usernametxt = Entry(adminlogin,font=('calibre',14,'normal'))
    usernametxt.pack()
    usernametxt.place(x=600,y=350)

    #passwordlabel
    passwordlabel = Label(adminlogin, text='Password',font= ('Helvetica 14 italic bold'))
    passwordlabel.pack()
    passwordlabel.place(x=600,y=400)
    passwordlabel.config(bg = "#010c20",fg="white")

    #password text entry
    passwordtxt = Entry(adminlogin,show='*',font=('calibre',14,'normal'))
    passwordtxt.pack()
    passwordtxt.place(x=600,y=450)

    def submit():
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
        sql = "SELECT * FROM administrator WHERE username = '%s' OR password = '%s'" %(username,password)
        c.execute(sql)
        row = c.fetchone()
        if row is None:
            messagebox.showinfo("Login Message", "Login Failed - Unable to fetch data")
        else:
            b1.adminid = row[0]
            b1.adminname = row[1]
            b1.username = row[2]
            b1.password = row[3]
            print("->Admin Login Successfully")
            amenu.dashboardpage()
        mydb.commit()
        mydb.close()

    createimg = PhotoImage(file="newaccountlogo.png",master=adminlogin)
    loginimg = PhotoImage(file="loginlogobtn.png",master=adminlogin)
    #loginbtn
    loginbtn = Button(adminlogin,image=loginimg,font= ('Helvetica 12 bold'),highlightthickness=0,borderwidth=0,bg='#010c20',fg='blue',command=submit)
    loginbtn.place(x=620,y=500)

    #create student rebtn
    createbtn = Button(adminlogin,image=createimg,font= ('Helvetica 12 bold'),highlightthickness=0,borderwidth=0,bg='#010c20',fg='blue',command=areg.adminregisterpage)
    createbtn.place(x=620,y=550)

    adminlogin.mainloop()
