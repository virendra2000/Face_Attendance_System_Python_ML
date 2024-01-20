import tkinter as tk
import staff.logindata as b1
from tkinter import messagebox
from about import *
from mysql import connector
from PIL import ImageTk,Image
from tkinter.filedialog import (askopenfilename, asksaveasfilename)
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
def stafflogin():
    userloginwind=Tk()
    userloginwind.title("Attendence Management System - User Login")
    userloginwind.geometry('1920x1080')
    userloginwind.configure(bg='#010c20')

    icoimg = PhotoImage(file="favicon.png",master=userloginwind)
    icolabel = Label(userloginwind,image=icoimg,bg="#010c20")
    icolabel.image = icoimg
    icolabel.place(x=650,y=20)

    label1 = Label(userloginwind, text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 bold'))
    label1.place(x=400,y=150)
    label1.config(bg = "#010c20",fg= "white")
    
    usernamevar = StringVar()
    passwordvar = StringVar()
    mainlabel = Label(userloginwind, text='USER LOGIN',font= ('Helvetica 20 italic bold'))
    mainlabel.place(x=600,y=250)
    mainlabel.config(bg = '#010c20',fg= "white")
    #usernamelabel
    usernamelabel = Label(userloginwind, text='USERNAME',font= ('Helvetica 14 italic bold'))
    usernamelabel.pack()
    usernamelabel.place(x=600,y=300)
    usernamelabel.config(bg = "#010c20",fg="white")
    #usernametxt
    usernametxt = Entry(userloginwind,textvariable=usernamevar,font=('calibre',14,'normal'))
    usernametxt.pack()
    usernametxt.place(x=600,y=350)
    #passwordlabel
    passwordlabel = Label(userloginwind, text='PASSWORD',font= ('Helvetica 14 italic bold'))
    passwordlabel.pack()
    passwordlabel.place(x=600,y=400)
    passwordlabel.config(bg = "#010c20",fg="white")
    #password text entry
    passwordtxt = Entry(userloginwind,show='*',textvariable=passwordvar,font=('calibre',14,'normal'))
    passwordtxt.pack()
    passwordtxt.place(x=600,y=450)
    def submit():
        username = usernamevar.get()
        password = passwordvar.get()
        conn = sqlite3.connect("attendencesystem.db")
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "' ")
        row = c.fetchone()
        if row is None:
            messagebox.showinfo("Login Message", "Login Failed - Unable to fetch data")
        else:
            b1.userid = row[0]
            b1.name = row[1]
            b1.address = row[2]
            b1.designation = row[3]
            b1.mobilenum = row[4]
            b1.emailid = row[5]
            b1.username = row[6]
            b1.password = row[7]
            messagebox.showinfo("Login Message", "Login Successfully")
            userdashboardpage()
        conn.commit()
        conn.close()
    loginimg = PhotoImage(file="loginlogobtn.png",master=userloginwind)
    loginbtn = Button(userloginwind, image=loginimg,text ="Login",font= ('Helvetica 12 bold'),highlightthickness=0,borderwidth=0,bg='#010c20',fg='blue',command=submit)
    loginbtn.image = loginimg
    loginbtn.place(x=620,y=500)
