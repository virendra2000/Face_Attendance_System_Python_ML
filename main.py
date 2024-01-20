from tkinter import *
from tkinter import messagebox
import about as info
from PIL import ImageTk,Image
import loginpage as lp

splash = Tk()
splash.title("Attendance Management System")
splash.geometry('1920x1080')
splash.config(bg="#010c20")
print("-> Welcome to Attendence Management Terminal Window")

splashlabel = Label(splash,bg="#010c20",fg='white',text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 italic bold'))
splashlabel.place(x=350,y=30)

img = Image.open('MGM_Institute_of_Health_Sciences_Logo.png')
img = img.resize((300, 300), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
iconlabel = Label(image=img,bg="#010c20")
iconlabel.place(x=500,y=150)

loginimg = PhotoImage(file="loginlogo.png")
aboutimg = PhotoImage(file="infologo.png")
exitimg = PhotoImage(file="exit.png")

def exit():
   splash.destroy()
   print("-> Thankyou for Connecting Our Terminal ! Visit Again !")

login = Button(splash,image=loginimg,text='Login',font= ('Helvetica 16 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command=lp.loginpagescreen)
login.place(x=400,y=500)

abt = Button(splash,image=aboutimg,text ="About",font= ('Helvetica 16 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command = info.aboutwin)
abt.place(x=600,y=500)

exitbtn = Button(splash,image=exitimg,text ="Exit",font= ('Helvetica 16 bold'),compound= TOP,borderwidth=0,bg='#010c20',fg='white',command = exit)
exitbtn.place(x=800,y=500)

def on_closing():
    splash.destroy()
    print("-> Interupt Occur while closing main window")
    print("<- Warning -> Please avoid closing main window while child window is Open")
splash.protocol("WM_DELETE_WINDOW", on_closing)
splash.mainloop()




