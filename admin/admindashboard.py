from tkinter import *
from tkinter import messagebox
from mysql import connector
import admin.logindata as b1
from PIL import ImageTk,Image
from tkinter.filedialog import (askopenfilename, asksaveasfilename)
import admin.createstudent as csa
import admin.createstaff as csta
import admin.createsubject as csbja
#admin dasboard initialize here
def dashboardpage():
        dashboard = Tk()
        dashboard.title("Admin Dashboard")
        dashboard.geometry("1920x1080")
        dashboard.configure(bg='#010c20')
        def logout():
           b1.adminid=""
           b1.adminname=""
           b1.username=""
           b1.password=""
           dashboard.destroy()
        icoimg = PhotoImage(file="favicon.png",master=dashboard)
        icolabel = Label(dashboard,image=icoimg,bg="#010c20")
        icolabel.image = icoimg
        icolabel.place(x=650,y=20)

        label1 = Label(dashboard, text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 bold'))
        label1.place(x=400,y=150)
        label1.config(bg = "#010c20",fg= "white")


        icoimg = PhotoImage(file="adminlogo.png",master=dashboard)
        icolabel = Label(dashboard,image=icoimg,bg="#010c20")
        icolabel.image = icoimg
        icolabel.place(x=50,y=200)
        
        #login detail will stored in one label i.e. loginname
        loginname = Label(dashboard, text=b1.adminname,font= ('Helvetica 18 italic bold'))
        loginname.pack()
        loginname.config(bg = "#010c20",fg= "white")
        loginname.place(x=180,y=250)

        logoutimg = PhotoImage(file="exit.png",master=dashboard)
        #logout button
        logoutbtn = Button(dashboard,image=logoutimg, text ="Logout",font= ('Helvetica 12 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command=logout)
        logoutbtn.image = logoutimg
        logoutbtn.place(x=1300,y=250)

        userimg = PhotoImage(file="userlogo.png",master=dashboard)
	#studentregistration button
        regbtn = Button(dashboard,image=userimg, text ="Create Student Registration",font= ('Helvetica 12 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command=csa.studregcomm)
        regbtn.image = userimg
        regbtn.place(x=160,y=400)

        userstaffimg = PhotoImage(file="stafflogo.png",master=dashboard)
        #create user button
        crtuserbtn = Button(dashboard,image=userstaffimg, text ="Create User",font= ('Helvetica 12 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command=csta.createstaffcomm)
        crtuserbtn.image = userstaffimg
        crtuserbtn.place(x=450,y=420)

        timeimg = PhotoImage(file="clock.png",master=dashboard)
        #set time and date
        settd = Button(dashboard,image=timeimg, text ="Set Date & Time",font= ('Helvetica 12 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white')
        settd.image = timeimg
        settd.place(x=650,y=390)

        subjimg = PhotoImage(file="book.png",master=dashboard)
        #create subject
       	crtsubj = Button(dashboard,image=subjimg, text ="Create Subject",font= ('Helvetica 12 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command=csbja.createsubjectfromadmin)
        crtsubj.image = subjimg
        crtsubj.place(x=850,y=390)

        attnd = PhotoImage(file="attendance.png",master=dashboard)
        #mark attendnce
       	mrkatt = Button(dashboard,image=attnd, text ="Mark Attendance",font= ('Helvetica 12 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command=csbja.createsubjectfromadmin)
        mrkatt.image = attnd
        mrkatt.place(x=1100,y=420)
