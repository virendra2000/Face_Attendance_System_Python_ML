import tkinter as tk
from tkinter import messagebox
from about import *
import staff.createsubject as css
from mysql import connector
from PIL import ImageTk,Image
from tkinter.filedialog import (askopenfilename, asksaveasfilename)
def userdashboardpage():
        dashboard = Tk()
        dashboard.title("Staff Dashboard")
        dashboard.geometry("500x500")
        dashboard.configure(bg='#010c20')
        loginname = Label(dashboard, text=b1.username,font= ('Helvetica 14 italic bold'))
        loginname.pack()
        loginname.config(bg = "#010c20",fg= "white")
        loginname.place(x=50,y=30)
        def logout():
            b1.userid = row[0]
            b1.name = row[1]
            b1.address = row[2]
            b1.mobilenum = row[4]
            b1.emailid = row[5]
            b1.username = row[6]
            b1.password = row[7]
            dashboard.destroy()
            userloginwind.destroy()
        #logout button
        logoutbtn = Button(dashboard, text ="Logout",font= ('Helvetica 12 bold'),borderwidth=0,bg='lime',fg='blue',command=logout)
        logoutbtn.place(x=400,y=30)
		
	createsubj = Button(dashboard,text="Create Subject",font= ('Helvetica 12 bold'),borderwidth=0,bg='lime',fg='blue',command=css.createsubjfromuser)
        createsubj.place(x=200,y=100)

        setdatetime = Button(dashboard,text="Set Date & Time",font= ('Helvetica 12 bold'),borderwidth=0,bg='lime',fg='blue')
        setdatetime.place(x=200,y=160)

        mrkattend = Button(dashboard,text="Mark Attendence",font= ('Helvetica 12 bold'),borderwidth=0,bg='lime',fg='blue')
        mrkattend.place(x=200,y=220)
