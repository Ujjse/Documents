#Creating a multi choice button radio button.
"""
from tkinter import*
window=Tk()
def add():
    print(var.get())
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,value=1,command=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="female",variable=var,value=2,command=add)
r2.pack(anchor=W)
window.mainloop()
"""

"""
from tkinter import *
window=Tk()
def add():
    print(var.get())
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,value=1,commmand=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
r2.pack(anchor=W)
window.mainloop()
"""

"""
from tkinter import*
root=Tk()
MODES=[("Pepperoni","Pepperoni"),("Cheese","Cheese"),("Mushroom","Mushroom"),("Onion","Onion")]
pizza=StringVar
pizza.set("Pepperoni")
for text, mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    myLabel=Label(root,text=value)
    myLabel.pack()

myButton=Button(root,text="Click",command=lambda :clicked(pizza.get()))
root.mainloop()
"""

"""
from tkinter import *
window=Tk()
def add():
    if var.get()==1:
        print("Male")
    else:
        print("Female")

var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,value=1,commmand=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
r2.pack(anchor=W)
window.mainloop()
"""

"""
from tkinter import*
window=Tk()
def add():
    selection="you have selected the optiom"+str(var.get())
    label.config(test=selection)
var=IntVar()
r1=Radiobutton(window,text="option 1",variable=var,value=1,command=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="Option 2",variable=var,value=2,command=add)
r2.pack(anchor=W)
r2=Radiobutton(window,text="Option 3",variable=var,value=2,command=add)
r2.pack(anchor=W)
label=Label(window)
label.pack()
window.mainloop()
"""

"""
from tkinter import *
top=Tk()
def add():
    label.config(test=CheckVar1.get())
CheckVar1=IntVar()
C1=Checkbutton(top,text="music",variable=CheckVar1, \
                onvalue=1,offvalue=0,height=5,\
                    width=20
                    )

C1.pack()
btn=Button(top,text="Click",command=add)
label=Label(top,text="")
label.pack()
btn.pack()
"""
"""
from tkinter import*
window=Tk()
def add():
    print(var.get())
var=IntVar()
r1=Radiobutton(window,text="male",variable=var,value=1,command=add)
#radiobutton is used to choose one option
r1.pack(anchor=W)
r2=Radiobutton(window,text="female",variable=var,value=2,command=add)
r2.pack(anchor=W)
window.mainloop()
"""

"""
from tkinter import*
window=Tk()
def add():
    if var.get()==1:
        print("Male")
    else:
        print("Female")
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,value=1,command=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
r2.pack(anchor=W)
window.mainloop()
"""