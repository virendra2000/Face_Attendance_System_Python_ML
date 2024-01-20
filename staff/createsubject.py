import tkinter as tk
from tkinter import messagebox
from about import *
from mysql import connector
from PIL import ImageTk,Image
from tkinter.filedialog import (askopenfilename, asksaveasfilename)
#createsubjfromuser function initialize
def createsubjfromuser():
    crtsubjframe = Tk()
    crtsubjframe.title("Government Of India - Create Subject")
    crtsubjframe.geometry('500x500')
    crtsubjframe.configure(bg='#010c20')
    subjectnamevar = StringVar()
                
    #toplevel main label
    crttitle = Label(crtsubjframe,text='Create Subject',font= ('Helvetica 20 italic bold'))
    crttitle.pack(pady=30)
    crttitle.config(bg="#010c20",fg="white")

    #subjname label
    subjctnamelbl = Label(crtsubjframe,text='Enter Subject Name',font = ('Helvetica 14 italic bold'))
    subjctnamelbl.pack(pady=30)
    subjctnamelbl.place(x=160,y=130)
    subjctnamelbl.config(bg="#010c20",fg="white")

    #subjname entry
    subjctnametxt = Entry(crtsubjframe,textvariable=subjectnamevar,font=('calibre',10,'normal'))
    subjctnametxt.pack(pady=30)
    subjctnametxt.place(x=160,y=160)

    #select branch label
    stdlbl = Label(crtsubjframe,text='Select Standard',font = ('Helvetica 14 italic bold'))
    stdlbl.pack(pady=30)
    stdlbl.place(x=160,y=200)
    stdlbl.config(bg="#010c20",fg="white")

    #select branch dropdown entry
    stdmenu = StringVar()
    stdmenu.set("Select Class")
    stdsubmenu = OptionMenu(crtsubjframe,stdmenu,"1","2","3","4","5","6","7","8","9","10")
    stdsubmenu.pack()
    stdsubmenu.place(x=160,y=230)

    def submit():
        subjectname = subjectnamevar.get()
        standard = stdmenu.get()
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Akil@123",
            database = "sysattendence"
        )
        c = mydb.cursor()
        sql = "INSERT INTO SUBJECT(subjectname,class) VALUES(%s,%s)"
        val = (subjectname,standard)
        c.execute(sql,val)
        mydb.commit()
        mydb.close()          
        messagebox.showinfo("Subject Creation", "Subject Created Successfully")
        subjectnamevar.set("")
        stdmenu.set("")
                    

    #create subject btn
    createsubbtn = Button(crtsubjframe, text ="Create",font= ('Helvetica 16 bold'),borderwidth=0,bg='lime',command = submit)
    createsubbtn.place(x=150,y=350)
