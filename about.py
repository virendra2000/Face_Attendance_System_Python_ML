from tkinter import *
from PIL import ImageTk,Image
def aboutwin():
    aboutwind = Tk()
    aboutwind.title("Attendence Management System - About")
    aboutwind.geometry('1920x1080')
    aboutwind.configure(bg='#010c20')
    print("->About Window Executed Successfully")
    ico = PhotoImage(file="favicon.png",master=aboutwind)
    icolabel = Label(aboutwind,image=ico,bg="#010c20")
    icolabel.place(x=650,y=20)
    backlogo = PhotoImage(file="back.png",master=aboutwind)

    def back():
       aboutwind.destroy()
       print("->About Window Exited Successfully")
    
    backbtn = Button(aboutwind,image=backlogo,text ="Back",font= ('Helvetica 16 bold'),compound=TOP,borderwidth=0,bg='#010c20',fg='white',command=back)
    backbtn.place(x=50,y=20)

    label1 = Label(aboutwind, text="MAHATMA GANDHI MISSION's\nCOLLEGE OF ENGINEERING & TECHNOLOGY",font= ('Helvetica 20 italic bold'))
    label1.place(x=400,y=150)
    label1.config(bg = "#010c20",fg= "white")
    info = '''
          Smart
	Education'''

    label2 = Label(aboutwind, text=info,font= ('Helvetica 20 bold'),justify= LEFT)
    label2.place(x=550,y=270)
    label2.config(bg = "#010c20",fg= "#BBA14F")

    message ='''
    Dear Students,

    

    Thanks & Regards,
    Team Techno Intelligence Squad 1 '''

    text_box = Text(aboutwind,height=10,width=40,bd=0,highlightthickness=0)
    text_box.place(x=480,y=400)
    text_box.insert('end', message)
    text_box.config(state='disabled',bg='white',fg='black',font= ('Helvetica 15 bold'))
    aboutwind.mainloop()



