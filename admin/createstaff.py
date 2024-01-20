import tkinter as tk
from tkinter import messagebox
from about import *
from mysql import connector
from PIL import ImageTk,Image
from tkinter.filedialog import (askopenfilename, asksaveasfilename)
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
def createstaffcomm():
    createuserframe = Tk()
    createuserframe.title("Government Of India - Create User")
    createuserframe.geometry('700x600')
    createuserframe.configure(bg='#010c20')
                
    #variable declaration start
    firstnamevar = StringVar()
    lastnamevar = StringVar()
    designationvar = StringVar()
    addressvar = StringVar()
    coursevar = StringVar()
    mobilenumvar = StringVar()
    emailaddvar = StringVar()
    usernamevar = StringVar()
    passwordvar = StringVar()
    #variable declaration end

    
    #main launcher logo
    userregwindlabel1 = Label(createuserframe, text='Create User',font= ('Helvetica 20 italic bold'))
    userregwindlabel1.pack(pady=30)
    userregwindlabel1.config(bg = "#010c20",fg= "white")
    
    #firstname label
    firstnamelbl = Label(createuserframe, text='First Name',font= ('Helvetica 12 italic bold'))
    firstnamelbl.pack()
    firstnamelbl.place(x=10,y=100)
    firstnamelbl.config(bg='#010c20',fg= "white")
    
    #firstname input text
    firstnametxt = Entry(createuserframe, textvariable=firstnamevar,font=('calibre',10,'normal'))
    firstnametxt.pack()
    firstnametxt.place(x=10,y=130)
    
    #lastname label
    lastnamelbl = Label(createuserframe, text='Last Name',font= ('Helvetica 12 italic bold'))
    lastnamelbl.pack(pady=20)
    lastnamelbl.place(x=170,y=100)
    lastnamelbl.config(bg='#010c20',fg= "white")

    #lastname input text
    lastnametxt = Entry(createuserframe,textvariable=lastnamevar,font=('calibre',10,'normal'))
    lastnametxt.pack()
    lastnametxt.place(x=170,y=130)

    #user designation label
    userdesignlbl = Label(createuserframe, text='Designation',font= ('Helvetica 12 italic bold'))
    userdesignlbl.pack(pady=20)
    userdesignlbl.place(x=10,y=160)
    userdesignlbl.config(bg='#010c20',fg= "white")

    #user designation entry
    userdesigntxt = Entry(createuserframe, textvariable=designationvar,font=('calibre',10,'normal'))
    userdesigntxt.pack()
    userdesigntxt.place(x=10,y=190)

    #address label
    addresslbl = Label(createuserframe, text='Address',font= ('Helvetica 12 italic bold'))
    addresslbl.pack(pady=20)
    addresslbl.place(x=170,y=160)
    addresslbl.config(bg='#010c20',fg= "white")

    #address input text
    addresstxt = Entry(createuserframe, textvariable=addressvar,font=('calibre',10,'normal'))
    addresstxt.pack()
    addresstxt.place(x=170,y=190)

    #mobile number label
    mobilenumlbl = Label(createuserframe, text='Student Mobile Number',font= ('Helvetica 12 italic bold'))
    mobilenumlbl.pack(pady=20)
    mobilenumlbl.place(x=10,y=220)
    mobilenumlbl.config(bg='#010c20',fg= "white")

    #mobile number input text
    mobilenumtxt = Entry(createuserframe, textvariable=mobilenumvar,font=('calibre',10,'normal'))
    mobilenumtxt.pack()
    mobilenumtxt.place(x=10,y=250)

    #email address label
    emailaddlbl = Label(createuserframe, text='Student Email Address',font= ('Helvetica 12 italic bold'))
    emailaddlbl.pack(pady=20)
    emailaddlbl.place(x=10,y=280)
    emailaddlbl.config(bg='#010c20',fg= "white")

    #email address input text
    emailaddtxt = Entry(createuserframe, textvariable=emailaddvar,font=('calibre',10,'normal'))
    emailaddtxt.pack()
    emailaddtxt.place(x=10,y=310)

    #username label
    usernamelbl = Label(createuserframe, text='Username',font= ('Helvetica 12 italic bold'))
    usernamelbl.pack(pady=20)
    usernamelbl.place(x=10,y=340)
    usernamelbl.config(bg='#010c20',fg= "white")

    #username input text
    usernametxt = Entry(createuserframe, textvariable=usernamevar,font=('calibre',10,'normal'))
    usernametxt.pack()
    usernametxt.place(x=10,y=370)

    #password label
    passwordlbl = Label(createuserframe, text='Password',font= ('Helvetica 12 italic bold'))
    passwordlbl.pack(pady=20)
    passwordlbl.place(x=10,y=400)
    passwordlbl.config(bg='#010c20',fg= "white")

    #password input text
    passwordtxt = Entry(createuserframe,show="*", textvariable=passwordvar,font=('calibre',10,'normal'))
    passwordtxt.pack()
    passwordtxt.place(x=10,y=430)

    #function declare to submit the data in database
    def  submit():
            print("-> Printing Data From User inputted")
            firstname = firstnamevar.get()
            lastname = lastnamevar.get()
            fullname = firstname +" " + lastname
            designation = designationvar.get()
            address = addressvar.get()
            mobilenum = mobilenumvar.get()
            emailadd = emailaddvar.get()
            username = usernamevar.get()
            password = passwordvar.get()
            passw = fernet.encrypt(password.encode())

            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Akil@123",
                database = "sysattendence"
            )
            c = mydb.cursor()
            sql = "INSERT INTO user(name,address,designation,mobilenum,emailid,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (fullname,address,designation,mobilenum,emailadd,username,passw)
            c.execute(sql,val)
            mydb.commit()
            mydb.close()
            messagebox.showinfo("Registration Message", "Successfully Submitted")
            
            firstnamevar.set("")
            lastnamevar.set("")
            designationvar.set("")
            addressvar.set("")
            mobilenumvar.set("")
            emailaddvar.set("")
            usernamevar.set("")
            passwordvar.set("")
            print("-> Create User Window is destroyed successfully after submitting detail")
            createuserframe.destroy()
            
    
    #register button set
    register = Button(createuserframe, text ="Register",font= ('Helvetica 16 bold'),borderwidth=0,bg='lime',command = submit)
    register.place(x=100,y=460)
