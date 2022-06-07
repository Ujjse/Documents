#It changes the shape
"""
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("white","white")
t.forward(150)
t.shapesize()
t.speed(6)
sc=turtle.Screen()
sc.title("Turtle")
sc.bgcolor("red")
turtle.screensize(900,900)
turtle.pensize(100)
t.clear()
turtle.done()


import turtle
sc=turtle.Screen()
t=turtle.Turtle()
t.left(75)
t.forward(100)
t.right(100)
t.forward(100)
t.left(10)
t.forward(100)
turtle.done()



import turtle
t=turtle.Turtle()
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.fd(100)

turtle.mainloop()
"""

"""
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range(4):
    pen.forward(50)
    pen.left(90)
turtle.done()
"""
"""
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range(5):
    pen.forward(100)
    pen.left(72)
turtle.done()
"""

"""
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range(6):
    pen.forward(100)
    pen.left(60)
turtle.done()
"""
"""
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range(7):
    pen.forward(100)
    pen.left(51.42)
turtle.done()

"""
"""
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range(8):
    pen.forward(100)
    pen.left(45)
turtle.done()
"""


"""
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range(9):
    pen.forward(100)
    pen.left(40)
turtle.done()


import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
pen.speed(0)
for i in range(50):
    pen.forward(100)
    pen.left(35)
turtle.done()
"""
"""
#to draw a circle
import turtle
t=turtle.Turtle()
t.circle(100)
turtle.done()
"""
"""
import turtle
t=turtle.Turtle()
t.dot(100)
turtle.done()



import turtle
t=turtle.Turtle()
t.up()
t.goto(0,-100)
t.down()
t.circle(100)
t.hideturtle()
turtle.done()

import turtle
turtle.seth(0)
turtle.forward(80)
turtle.write("East")
turtle.home()
turtle.setheading(90)
turtle.forward(80)
turtle.write("North")
turtle.home()
turtle.seth(180)
turtle.forward(80)
turtle.write("West")
turtle.home()
turtle.setheading(270)
turtle.forward(80)
turtle.write("South")
turtle.ht()
turtle.done()
"""

'''
import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
while (True):
    for i in range(6):
        for colors in["red", "blue", "magneta", "green", "yellow", "white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)
    break
turtle.mainloop()
'''

'''
import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
while (True):
    for i in range(6):
        for colors in ["red","blue","magenta","green","yellow","white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)
    break
turtle.mainloop()
'''

"""
#Making a star.
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range (5):
    pen.forward(100)
    pen.right(144)
    pen.ht()
turtle.done()
"""


"""
#Making 5 circles.
import turtle
t=turtle.Turtle()
t.up()
t.goto(0,-100)
t.down()
t.circle(100)
t.up()
t.goto(300,100)
t.down()
t.circle(100)
t.up()
t.goto(-300,100)
t.down()
t.circle(100)
t.up()
t.goto(300,-300)
t.down()
t.circle(100)
t.up()
t.goto(-300,-300)
t.down()
t.circle(100)
t.hideturtle()
turtle.done()
"""


"""
#for full screen.
import turtle
t=turtle.Turtle()
turtle.bgcolor("blanchedalmond")
t.begin_fill()
t.fillcolor("Red")
t.up()
t.goto(0,-100)
t.down()
t.circle(100)
t.end_fill()
t.begin_fill()
t.fillcolor("Pink")
t.up()
t.goto(600,200)
t.down()
t.circle(100)
t.end_fill()
t.begin_fill()
t.fillcolor("White")
t.up()
t.goto(-600,200)
t.down()
t.circle(100)
t.end_fill()
t.begin_fill()
t.fillcolor("magenta")
t.up()
t.goto(600,-400)
t.down()
t.circle(100)
t.end_fill()
t.begin_fill()
t.fillcolor("cyan")
t.up()
t.goto(-600,-400)
t.down()
t.circle(100)
t.end_fill()
t.hideturtle()
t.end_fill()
turtle.done() 
"""

"""
from tkinter import *
win=Tk()
win.geometry("400x250")
win.title("HELLO")
win.geometry('600x300')
name=Label(win,text="Name").grid(row=0,column=0)
e1=Entry(win).grid(row=0,column=1)
password=Label(win,text="Password").grid(row=1,column=0)
e2=Entry(win).grid(row=1,column=1)
submitButton=Button(win,text="Submit").grid(row=4,column=1)
win.configure(bg="red")
win.mainloop()
"""
"""
from tkinter import *
win=Tk()
win.title("HELLO")
win.geometry('600x300')
redButton=Button(win,text = "Sighn Up", fg="green")
redButton.pack(side=RIGHT)
win.mainloop()
"""

"""
from tkinter import *
win=Tk()
win.geometry("400x250")
win.title("HELLO")
win.geometry('600x300')
name=Label(win,text="Name").grid(row=0,column=0)
e1=Entry(win).grid(row=0,column=1)
password=Label(win,text="Password").grid(row=1,column=0)
e2=Entry(win).grid(row=1,column=1)
submitButton=Button(win,text="Submit").grid(row=4,column=1)
win.configure(bg="red")
win.mainloop()
"""



"""
from tkinter import *
root=Tk()
text=Button(root,text="PYTHON")
text.pack(side=)
font=90
root.mainloop()
"""

"""
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Sighn Up Page")
root.geometry("400x250")
usrname=Label(root, bg="White",text="Username",fg="Black").place(x=40,y=30)
e1=Entry(root).place(x=120,y=30)
email=Label(root,bg="white",text="Email",fg="Black").place(x=40,y=60)
e1=Entry(root).place(x=120,y=60)
email=Label(root,bg="White",text="Age",fg="Black").place(x=40,y=90)
e1=Entry(root).place(x=120,y=90)
Dob=Label(root,bg="White",text="Date Of birth",fg="Black").place(x=30,y=120)
e1=Entry(root).place(x=120,y=120)
password=Label(root,bg="White",text="Password",fg="Black").place(x=40,y=150)
e2=Entry(root).place(x=120,y=150)
password2=Label(root,bg="White",text="Confirm Password",fg="Black").place(x=5
,y=180)
e2=Entry(root).place(x=120,y=180)
sighnup=Button(root,text="Sighn Up",bg="Black").place(x=150,y=210)
root.configure(bg="White")
image_0=Image.open("/Users/ujjwalpariyar/Downloads/material-style-8k-2560x1600.jpg")
bck_end=ImageTk.PhotoImage(image_0)
root.mainloop()
"""