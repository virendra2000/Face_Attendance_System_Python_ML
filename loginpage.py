from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from admin import adminlogin as al
from staff import stafflogin as sl
def loginpagescreen():
    loginwind = Tk()
    loginwind.title("Attendence Management System - Login Page")
    loginwind.geometry('1920x1080')
    loginwind.configure(bg='#010c20')
    print("->Login Page Executed Successfully")
    ico = PhotoImage(file="favicon.png",master=loginwind)
    icolabel = Label(loginwind,image=ico,bg="#010c20")
    icolabel.place(x=650,y=20)

    label1 = Label(loginwind, text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 bold'))
    label1.place(x=400,y=150)
    label1.config(bg = "#010c20",fg= "white")

    mainlabel = Label(loginwind, text='LOGIN MENU',font= ('Helvetica 20 bold'))
    mainlabel.place(x=600,y=250)
    mainlabel.config(bg = '#010c20',fg= "white")

    adminllogo = PhotoImage(file="adminlogo.png",master=loginwind)
    staffllogo = PhotoImage(file="stafflogo.png",master=loginwind)
    backlogo = PhotoImage(file="back.png",master=loginwind)

    def back():
       loginwind.destroy()
       print("->Login Window Exited Successfully");

    adminlgnbtn = Button(loginwind,image=adminllogo,text="Admin Logo",font= ('Helvetica 16 bold'),compound=TOP,borderwidth=0,bg='#010c20',fg='white',command=al.adminloginpage)
    adminlgnbtn.place(x=450,y=350)

    crtuserbtn = Button(loginwind,image=staffllogo,text ="Staff Login",font= ('Helvetica 16 bold'),compound=TOP,borderwidth=0,bg='#010c20',fg='white',command = sl.stafflogin)
    crtuserbtn.place(x=650,y=350)

    backbtn = Button(loginwind,image=backlogo,text ="Back",font= ('Helvetica 16 bold'),compound=TOP,borderwidth=0,bg='#010c20',fg='white',command=back)
    backbtn.place(x=850,y=350)
    loginwind.mainloop()