import tkinter as tk
from tkinter import messagebox
from about import *
from mysql import connector
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from cryptography.fernet import Fernet
import mysql.connector as mysql
key = Fernet.generate_key()
fernet = Fernet(key)
def studregcomm():
    studregframe = Tk()
    studregframe.title("Student Registration")
    studregframe.geometry('1920x1080')
    studregframe.configure(bg='#010c20')

    icoimg = PhotoImage(file="favicon.png",master=studregframe)
    icolabel = Label(studregframe,image=icoimg,bg="#010c20")
    icolabel.image = icoimg
    icolabel.place(x=650,y=20)

    label1 = Label(studregframe, text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 bold'))
    label1.place(x=400,y=150)
    label1.config(bg = "#010c20",fg= "white")
    
    #main launcher logo
    studregwindlabel1 = Label(studregframe, text='Student Registration',font= ('Helvetica 20 italic bold'))
    studregwindlabel1.place(x=600,y=250)
    studregwindlabel1.config(bg = "#010c20",fg= "white")
    
    #firstname label
    firstnamelbl = Label(studregframe, text='First Name',font= ('Helvetica 14 italic bold'))
    firstnamelbl.pack()
    firstnamelbl.place(x=500,y=350)
    firstnamelbl.config(bg='#010c20',fg= "white")
    
    #firstname input text
    firstnametxt = Entry(studregframe,font=('calibre',14,'normal'))
    firstnametxt.pack()
    firstnametxt.place(x=500,y=380)
    
    #lastname label
    lastnamelbl = Label(studregframe, text='Last Name',font= ('Helvetica 14 italic bold'))
    lastnamelbl.pack()
    lastnamelbl.place(x=750,y=350)
    lastnamelbl.config(bg='#010c20',fg= "white")

    #lastname input text
    lastnametxt = Entry(studregframe, font=('calibre',14,'normal'))
    lastnametxt.pack()
    lastnametxt.place(x=750,y=380)

    #roll number label
    rollnumlbl = Label(studregframe, text='Roll Number',font= ('Helvetica 14 italic bold'))
    rollnumlbl.pack()
    rollnumlbl.place(x=500,y=430)
    rollnumlbl.config(bg='#010c20',fg= "white")

    #roll number input text
    rollnumtxt = Entry(studregframe,font=('calibre',14,'normal'))
    rollnumtxt.pack()
    rollnumtxt.place(x=500,y=460)

    #address label
    addresslbl = Label(studregframe, text='Address',font= ('Helvetica 14 italic bold'))
    addresslbl.pack()
    addresslbl.place(x=750,y=430)
    addresslbl.config(bg='#010c20',fg= "white")

    #address input text
    addresstxt = Entry(studregframe, font=('calibre',14,'normal'))
    addresstxt.pack()
    addresstxt.place(x=750,y=460)

    #student mobile number label
    mobilenumlbl = Label(studregframe, text='Student Mobile Number',font= ('Helvetica 14 italic bold'))
    mobilenumlbl.pack()
    mobilenumlbl.place(x=500,y=500)
    mobilenumlbl.config(bg='#010c20',fg= "white")

    #student mobile number input text
    mobilenumtxt = Entry(studregframe, font=('calibre',14,'normal'))
    mobilenumtxt.pack()
    mobilenumtxt.place(x=500,y=530)

    #student email address label
    emailaddlbl = Label(studregframe, text='Student Email Address',font= ('Helvetica 14 italic bold'))
    emailaddlbl.pack()
    emailaddlbl.place(x=750,y=500)
    emailaddlbl.config(bg='#010c20',fg= "white")

    #student  email address input text
    emailaddtxt = Entry(studregframe, font=('calibre',14,'normal'))
    emailaddtxt.pack()
    emailaddtxt.place(x=750,y=530)

    deptlist = ["Computer Engineering","Mechanical Engineering","Civil Engineering","Chemical ENgineering","Electronics & Telecommunication ENgineering","ELectrical Engineering","Information Technology"]
    #department options
    departmentlbl = Label(studregframe, text='Select Department',font= ('Helvetica 14 italic bold'))
    departmentlbl.pack()
    departmentlbl.place(x=500,y=560)
    departmentlbl.config(bg='#010c20',fg= "white")

    stdmenu = StringVar()
    stdmenu.set("Select Department")
    stddeptmenu = OptionMenu(studregframe,stdmenu,*deptlist)
    stddeptmenu.pack()
    stddeptmenu.place(x=500,y=590)

    #class options
    classlbl = Label(studregframe, text='Select Class',font= ('Helvetica 14 italic bold'))
    classlbl.pack()
    classlbl.place(x=750,y=560)
    classlbl.config(bg='#010c20',fg= "white")

    stdtmenu = StringVar()
    stdtmenu.set("Select Class")
    stdclassmenu = OptionMenu(studregframe,stdtmenu,"FE","SE","TE","BE")
    stdclassmenu.pack()
    stdclassmenu.place(x=750,y=590)

    global filename # Access this from both functions
    def upload_file(): # Image upload and display
        global filename,img
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
    


    #function declare to submit the data in database
    def  submit():
        print("-> Printing Data From User inputted")
        firstname = firstnametxt.get()
        lastname = lastnametxt.get()
        fullname = firstname +" " + lastname
        rollnumber = rollnumtxt.get()
        addressval = addresstxt.get()
        mobilenum = mobilenumtxt.get()
        emailadd = emailaddtxt.get()
        dept = stdmenu.get()
        classval = stdtmenu.get()
        global img , filename 
        fob=open(filename,'rb') # filename from upload_file()
        fob=fob.read()
        mydb = mysql.connect(
            host = "localhost",
            user = "root",
            password = "Rootadmin@2023",
            database = "sysattendence"
        )
        c = mydb.cursor()
        sql = "INSERT INTO student(name,rollnum,address,mobilenum,email,department,class,profileimage) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (fullname,rollnumber,addressval,mobilenum,emailadd,dept,classval,fob)
        c.execute(sql,val)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Registration Message", "Successfully Submitted")
    
    #upload button set
    browsebtn = Button(studregframe, text ="Browse",font= ('Helvetica 16 bold'),borderwidth=0,bg='lime',command = upload_file)
    browsebtn.place(x=600,y=650)
    #register button set
    register = Button(studregframe, text ="Register",font= ('Helvetica 16 bold'),borderwidth=0,bg='lime',command = submit)
    register.place(x=700,y=650)
