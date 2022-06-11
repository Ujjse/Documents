from _ast import Lambda #It is a anonymous function which can take any number of arguments but can have only one expression.
from ast import operator
from tkinter import *
#tkinter is a gui application
root = Tk() #Calling Tk()
text_Input=StringVar()
root.config(bg="black")
root.title ("Simple Calculator")#Naming The calculator.
e= Entry(root, width=35, borderwidth=5,textvariable=text_Input,bd=10,fg="Black",bg="White")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
operator=" " #Setting operator empty so that the user can change the operator accordingly.


#Creating function to pass the numbers.  
def button_click(number):
    global operator
    operator=operator+str(number)
    text_Input.set(operator)

#Creating function for clearing the output and input screen of calculator
def button_clear():
    global operator
    operator=" "
    text_Input.set(" ")

#Function to show the ans using equal to button sighn.
def button_equal():
    global operator
    calc=str(eval(operator))#Evaluating the value of operator and passing it to calc
    text_Input.set(calc)
    operator=" "


#Creating buttons.
#we have passed command=lambda to create anonymous function.
button_1 = Button(root, text="1",padx=40, pady=20, command=lambda : button_click(1))
button_2 = Button(root, text="2",padx=40, pady=20, command=lambda : button_click(2))
button_3 = Button(root, text="3",padx=40, pady=20, command=lambda : button_click(3))
button_4 = Button(root, text="4",padx=40, pady=20, command=lambda : button_click(4))
button_5 = Button(root, text="5",padx=40, pady=20, command=lambda : button_click(5))
button_6 = Button(root, text="6",padx=40, pady=20, command=lambda : button_click(6))
button_7 = Button(root, text="7",padx=40, pady=20, command=lambda : button_click(7))
button_8 = Button(root, text="8",padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9",padx=40, pady=20, command=lambda : button_click(9))
button_0 = Button(root, text="o",padx=40, pady=20, command=lambda: button_click(0))
button_add=Button(root, text="+",padx=40, pady=20,fg="Green", command=lambda:button_click("+"))
minus = Button(root, text='-', padx=40, pady=20, fg='Green',command=lambda: button_click("-"))
multiply = Button(root, text='*',padx=40, pady=20, fg='Green',command=lambda:button_click("*")) 
divide = Button(root, text='/',fg="Green",padx=40, pady=20,command=lambda: button_click("/"))
button_equal= Button(root,text="=",fg="Green",bg="Green",padx=40, pady=20, command=button_equal)
button_clear= Button(root,bd=10, relief='raised',overrelief='groove',text="Clear",fg="Red", padx=150, pady=20,command=button_clear)
 
#putting buttons on screen.
#Placing the buttons.
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3. grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=6,column=0,columnspan=3)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1)

multiply.grid(row=4, column=1)
divide.grid(row=4, column=2)
minus.grid(row=5, column=2)

root.mainloop()