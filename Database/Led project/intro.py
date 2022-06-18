from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title=("Introduction")

root.configure=bg=(ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/italian-foods-concept-menu-design-2528848.jpg")))

# ttle=Label(root,text="SUMS",fg="White",font=("Ariel",30))
# ttle.place(x=0,y=1)

# log_btn=Button(root,text="Log in")
# log_btn.place(x=100,y=1)

root.mainloop()