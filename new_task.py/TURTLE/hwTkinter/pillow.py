""""
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
my_Image=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/media_16ad2258cac6171d66942b13b8cd4839f0b6be6f3.png"))
myLabel=Label(image=my_Image)
myLabel.pack()
button_quit=Button(root,text="Exit",command=root.quit,width=20)
button_quit.pack()
root.mainloop()
"""
"""
from tkinter import*
window=Tk()
window.geometry("300*300")
bg=PhotoImage(file="/Users/ujjwalpariyar/Downloads/media_16ad2258cac6171d66942b13b8cd4839f0b6be6f3.png")
my_label=Label(window,image=bg)
my_label.pack()
window.mainloop()
"""


"""  
#code to resize an image
from tkinter import*
from PIL import Image, ImageTk
window=Tk()
window.title("LOGIN")
window.maxsize(width=300,height=200)
window.minsize(width=300,height=200)
my_image=Image.open("/Users/ujjwalpariyar/Downloads/ndYhJu.jpg")
resized_image=my_image.resize((300,250))
converted_image=ImageTk.PhotoImage(resized_image)

mylabel=Label(window,image=converted_image,width=300,height=180)
mylabel.pack()
btn=Button(window,text="exit",command=window.quit,width=20)
btn.pack()
window.mainloop()
"""

"""
from tkinter import * 
root=Tk()

def call():
    label=Label(root,text="You just clicked")
    label.pack()

button=Button(root,text="Click me",command=call)
button.pack()
label=Label(root,text="Hello",fg="White")
label.pack()
root.mainloop()

root=Tk()
"""



"""
from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.title("LOGIN")
my_image=Image.open("/Users/ujjwalpariyar/Downloads/ndYhJu.jpg")
resized_image=my_image.resize((300,250))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
window.mainloop()
"""

"""
#To pop up a message box after a click
from tkinter import* 
from tkinter import messagebox
root=Tk()

def popup():
    messagebox.showinfo("This is my popup","Hello World")

btn=Button(root,text="popup",command=popup).pack()
root.mainloop()
"""


"""
#To make a pop up box with choices.
from tkinter import* 
from tkinter import messagebox
root=Tk()

def popup():
    response=messagebox.askyesno("This is my popup","Hello World")
    #The first string this is pop up is the title and the hello world shows in the pop up box.
    Label(root,text=response).pack()

    if response==1:
        Label(root,text="Clicked Yes").pack()
    else:
        Label(root,text="Clicked no").pack()


btn=Button(root,text="popup",command=popup).pack()
root.mainloop()
"""
"""

from tkinter import*
from PIL import Image,ImageTk
root=Tk()
def open():
    global my_img
    top=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/ndYhJu.jpg"))
    my_label=Label(top,image=my_img)
    my_label.pack()
    btn=Button(top,text="Close Window",command=top.destroy)
    btn.pack()
btnn=Button(root,text="open",command=open)
btnn.pack()
root.mainloop()
"""


"""
from tkinter import*
root=Tk()
root.geometry("200x200")
def show():
    label.config(text=clicked.get())

options=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
clicked=StringVar()
clicked.set("Monday")
 
drop=OptionMenu(root,clicked,*options)
drop.pack()

button=Button(root, text="Click Me", command=show).pack()
label=Label(root,text=" ")
label.pack()
root.mainloop()
"""


"""
from tkinter import*
from tkinter.font import BOLD
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
my_Image=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/ndYhJu.jpg"))
myLabel=Label(image=my_Image)
myLabel.pack()
titlename=Label(root,text="Welcome to Sighnup Page",fg="White",font=("Ariel",30,BOLD),bg="black").place(x=575,y=70)
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
def popup():
    messagebox.showinfo("You are being Sighned in","Sighning in")
sighn=Button(root,text="Sighn in",fg="Black",command=popup).place(x=710,y=505)
root.mainloop()
"""


from tkinter import*
root=Tk()
root.geometry("640x900")
root.title=("Calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X, ipadx=8,pady=10,padx=10)

f=Frame(root,bg="Grey")
b=Button(f,text="g",padx=28,pady=22,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)



root.mainloop()