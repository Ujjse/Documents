"""
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk,Image
root=Tk()
root.title("Sighn Up Page")
root.geometry("400x250")
my_Image=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/material-style-8k-2560x1600.jpg"))
myLabel=Label(image=my_Image)
myLabel.pack()
root.iconbitmap("/Users/ujjwalpariyar/Documents/new_task.py/newhomework.py/ujj.ico")
titlename=Label(root,bg="White",text="Welcome to FoodHub",fg="LimeGreen",font=("Ariel",30,BOLD)).place(x=590,y=100)
usrname=Label(root, bg="White",text="Username",fg="Black").place(x=540,y=330)
e1=Entry(root).place(x=660,y=330)
email=Label(root,bg="white",text="Email",fg="Black").place(x=540,y=360)
e1=Entry(root).place(x=660,y=360)
email=Label(root,bg="White",text="Age",fg="Black").place(x=540,y=390)
e1=Entry(root).place(x=660,y=390)
Dob=Label(root,bg="White",text="Date Of birth",fg="Black").place(x=540,y=420)
e1=Entry(root).place(x=660,y=420)
password=Label(root,bg="White",text="Password",fg="Black").place(x=540,y=450)
e2=Entry(root).place(x=660,y=450)
password2=Label(root,bg="White",text="Confirm Password",fg="Black").place(x=540,y=480)
e2=Entry(root).place(x=660,y=480)
def click():
    myLabel=Label(root, text="Your data is being saved,Please Wait.",fg="Red")
    myLabel.place(x=650,y=600)
sighnn=Button(root,text="Sighn Up",bg="White",fg="Black",command=click)
sighnn.place(x=710,y=570)
root.configure(bg="White")
root.mainloop()
"""

"""
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk,Image
root=Tk()
root.title("Sighn Up Page")
root.geometry("400x250")
my_Image=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/material-style-8k-2560x1600.jpg"))
myLabel=Label(image=my_Image)
myLabel.pack()
root.iconbitmap("/Users/ujjwalpariyar/Documents/new_task.py/newhomework.py/ujj.ico")
titlename=Label(root,bg="White",text="Welcome to FoodHub",fg="LimeGreen",font=("Ariel",30,BOLD)).place(x=590,y=100)
usrname=Label(root, bg="White",text="Username",fg="Black",font=("Ariel",20,BOLD)).place(x=50,y=330)
e1=Entry(root).place(x=170,y=330)
email=Label(root,bg="white",text="Email",fg="Black",font=("Ariel",20,BOLD)).place(x=540,y=360)
e1=Entry(root).place(x=660,y=360)
email=Label(root,bg="White",text="Age",fg="Black",font=("Ariel",20,BOLD)).place(x=540,y=390)
e1=Entry(root).place(x=660,y=390)
Dob=Label(root,bg="White",text="Date Of birth",fg="Black",font=("Ariel",20,BOLD)).place(x=540,y=420)
e1=Entry(root).place(x=660,y=420)
password=Label(root,bg="White",text="Password",fg="Black",font=("Ariel",20,BOLD)).place(x=540,y=450)
e2=Entry(root).place(x=660,y=450)
password2=Label(root,bg="White",text="Confirm Password",fg="Black",font=("Ariel",20,BOLD)).place(x=540,y=480)
e2=Entry(root).place(x=660,y=480)
def click():
    myLabel=Label(root, text="Your data is being saved,Please Wait.",fg="Red")
    myLabel.place(x=650,y=600)
sighnn=Button(root,text="Sighn Up",bg="White",fg="Black",command=click)
sighnn.place(x=710,y=570)
root.configure(bg="White")
root.mainloop()
"""

"""
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk,Image
root=Tk()
root.title("Sighn Up Page")
root.geometry("400x250")
root.iconbitmap("/Users/ujjwalpariyar/Documents/new_task.py/newhomework.py/ujj.ico")
my_Image=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/6169319.jpg"))
myLabel=Label(image=my_Image)
myLabel.pack()
titlename=Label(root,text="Welcome to Sighnup Page",fg="White",font=("Ariel",30,BOLD),bg="Red").place(x=590,y=70)
usrname=Label(root, bg="White",text="Username",fg="Black").place(x=540,y=328)
e1=Entry(root,bg="White",fg="Black").place(x=660,y=325)
email=Label(root,bg="White",text="Email",fg="Black").place(x=540,y=358)
e1=Entry(root,bg="White",fg="Black").place(x=660,y=355)
email=Label(root,text="Age",bg="White",fg="Black").place(x=540,y=388)
e1=Entry(root,bg="White",fg="Black").place(x=660,y=385)
Dob=Label(root,text="Date Of birth",bg="White",fg="Black").place(x=540,y=418)
e1=Entry(root,bg="White",fg="Black").place(x=660,y=415)
password=Label(root,text="Password",fg="Black",bg="White").place(x=540,y=448)
e2=Entry(root,bg="White",fg="Black").place(x=660,y=445)
password2=Label(root,text="Confirm Password",fg="Black",bg="White").place(x=540,y=478)
e2=Entry(root,bg="White",fg="Black").place(x=660,y=475)
def click():
    myLabel=Label(root, text="Your data is being saved,Please Wait.",fg="Red")
    myLabel.place(x=650,y=600)
sighnn=Button(root,text="Sighn Up",bg="Red",fg="Black",command=click)
sighnn.place(x=710,y=570)
root.configure(bg="White")
root.mainloop()
"""

"""
#Disabling a button.
from tkinter import*
root=Tk()
e1=Button(root,text="Click").place(x=20,y=30)
e2=Button(root,text="Click").place(x=20,y=60)
e3=Button(root,text="Click").place(x=20,y=90)
e4=Button(root,text="Click",state=DISABLED).place(x=20,y=120)
root.mainloop()

"""


"""

#To add a text with a click
#It adds a text + the message that you have entered in the entry label.
#It is useful for the times to display a message according to the 

from tkinter import* 
window=Tk()
e=Entry(window,width=50,bg="White",fg="Black",borderwidth=5,font=20)
e.pack()
def myClick():
    my_label=Label(window,text="hello "+e.get())
    my_label.pack()
    
btn=Button(window,text="Click me",padx=10,pady=10,command=myClick)
btn.pack()
window.mainloop()
"""

"""
from tkinter import *
root=Tk()
root.title("GUI")
root.maxsize(width=600,height=300)
root.minsize(width=600,height=300)
def add():
    x=var.get()
    print(x)
    mylabell.config(text=x,bg="green")
#label1
mylabel=Label(root,text="Username",fg="red",bg="yellow")
mylabel.place(x=10,y=10)
#label2
mylabell=Label(root,text="Nothing",fg="red",bg="yellow")#here the text="nothing" it is called conig method.
mylabell.place(x=40,y=120)
#entry button
var=StringVar()
ent=Entry(root,bg="black",fg="white",textvariable=var)
ent.place(x=80,y=10)
btn=Button(root, text="Submit", bg="green", fg="white", command=add)
btn.place(x=20, y=80)
root.mainloop()
"""

"""
from tkinter import*
root=Tk()
def click():
    text1="Address"+mytext.get("5.0",END)
    lbl.config(text=str(text1))

mytext=Text(root,font=20,width=20,height=10)
mytext.place(x=0,y=50)

btn=Button(root,text="Click me",font=30,command=click)
btn.place(x=400,y=300)

lbl=Label(root,text="",font=30)
lbl.place(x=200,y=300)

root.mainloop()
"""  

"""
from tkinter import*
window=Tk()
frame=LabelFrame(window,text="This is my frame",padx=10,pady=10)
frame.pack(padx=50,pady=50)
b=Button(frame,text="Dont Click here")
b2=Button(frame,text=".....here")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)
window.mainloop()

"""