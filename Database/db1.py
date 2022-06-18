from tkinter import*
import sqlite3
from tkinter import messagebox

root=Tk()

conn=sqlite3.connect('address_book.db')
c=conn.cursor()

#Here we do c=execute so to create a new table.
c.execute(""" CREATE TABLE address(      
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")
print("Table is created succesfully.")

def submit():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()

    c.execute("INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })
    messagebox.showinfo("Address","Inserted successfully")

    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def delete():
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()

    c.execute("DELETE from address WHERE oid="+delete_box.get())
    print("Deleted Successfully")
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute(""" UPDATE address SET
        first_name= :first, 
        last_name=:last,
        address=:adress,
        city=:city,
        state=:state,
        zipcode=:zipcode
        WHERE oid=:oid """,
        {'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'adress':address_editor.get(),
        'city':city_editor.get(),
        'state':state_editor.get(),
        'zipcode':zipcode_editor.get(),
        'oid':record_id
        }
    )
    conn.commit()
    conn.close()
    editor.destroy()

def query():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute("SELECT * , oid FROM address")
    records=c.fetchall()
    print(records)

    print_record=" "
    for record in records:
        print_record+=str(record[0])+" "+ str(record[1])+" " + "\t" + str(record[6])+ "\n"

    query_label=Label(root,text=print_record)
    query_label.grid(row=11,column=0,columnspan=2)

    conn.commit()
    conn.close()

def edit():
    global editor
    editor=Toplevel()
    editor.title("Update data")
    editor.geometry('300x400')
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM address WHERE oid=" + record_id)
    records=c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # f1_name_editor=Entry(editor,width=30)
    # f1_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=1,column=1)

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=2,column=1)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=3,column=1)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=4,column=1)

    state_editor=Entry(editor,width=30)
    state_editor.grid(row=5,column=1)

    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=6,column=1)

    #labelling of those code

    f_name_label=Label(editor,text='Full Name')
    f_name_label.grid(row=1,column=0,pady=(10,0))

    l_name_label=Label(editor,text="Last Name")
    l_name_label.grid(row=2,column=0)

    address_label=Label(editor,text="Address")
    address_label.grid(row=3,column=0)

    city_label=Label(editor,text='City')
    city_label.grid(row=4,column=0)

    state_label=Label(editor,text="State")
    state_label.grid(row=5,column=0)

    zipcode_label=Label(editor,text="Zipcode")
    zipcode_label.grid(row=6,column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    
    edit_btn=Button(editor,text='Save',command=update)
    edit_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=12)
    conn.commit()
    conn.close()
#Creating for inside

f_name=Entry(root,width=30)
f_name.grid(row=3,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=2,column=1)


address=Entry(root,width=30)
address.grid(row=4,column=1)

city=Entry(root,width=30)
city.grid(row=5,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=6,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=7,column=1,padx=20)

delete_box=Entry(root,width=30)
delete_box.grid(row=10,column=0,columnspan=2,pady=10, ipadx=20)

#Textbox labels


f_name_label=Label(root,text="First Name")
f_name_label.grid(row=2,column=0)

l_name_label=Label(root,text="last Name")
l_name_label.grid(row=3,column=0)

address_label=Label(root,text="Address Name")
address_label.grid(row=4,column=0)

city_label=Label(root,text="City Name")
city_label.grid(row=5,column=0)

state_label=Label(root,text="state Name")
state_label.grid(row=6,column=0)

zipcode_label=Label(root,text="zipcode")
zipcode_label.grid(row=7,column=0)

submit_btn=Button(root,text="Add records", command=submit)
submit_btn.grid(row=8,column=0,columnspan=2,pady=10,ipadx=100)

query_btn=Button(root,text="Query",command=query)
query_btn.grid(row=9,column=0,columnspan=2,pady=10, ipadx=100)

del_btn=Button(root,text="Delete",command=delete)
del_btn.grid(row=11,column=0,columnspan=2,pady=10, ipadx=100)

btn=Button(root,text="Update",command=edit)
btn.grid(row=12,column=0,columnspan=2,pady=10,ipadx=100)
conn.commit()
conn.close()

root.mainloop()


# from tkinter import*
# import sqlite3
# from tkinter import messagebox

# root=Tk()
# root.title("Facebook")
# conn=sqlite3.connect('facebook.db')
# c=conn.cursor()

# c.execute(""" CREATE TABLE user(      
#     first_name text,
#     last_name text,
#     address text,
#     age text,
#     password text,
#     father_name text,
#     city text,
#     zipcode integer
#  )""")
# print("Table is created succesfully.")


# #Labelling of the table
# first_name=Label(root,text="First Name")
# first_name.grid(row=1,column=0)

# last_name=Label(root,text="Last Name")
# last_name.grid(row=2,column=0)

# address=Label(root,text="Address")
# address.grid(row=3,column=0)

# age=Label(root,text="Age")
# age.grid(row=4,column=0)

# password=Label(root,text="First Name")
# password.grid(row=5,column=0)

# city=Label(root,text="city")
# city.grid(row=6,column=0)

# father_name=Label(root,text="Fathers Name")
# father_name.grid(row=7,column=0)

# zipcode=Label(root,text="Zipcode")
# zipcode.grid(row=8,column=0)





# #Entry of the table
# first_name=Entry(root,width=30)
# first_name.grid(row=1,column=1)

# last_name=Entry(root,width=30)
# last_name.grid(row=2,column=1)

# address=Entry(root,width=30)
# address.grid(row=3,column=1)

# age=Entry(root,width=30)
# age.grid(row=4,column=1)

# password=Entry(root,width=30)
# password.grid(row=5,column=1)

# city_editor=Entry(root,width=30)
# city_editor.grid(row=6,column=1)

# father_name=Entry(root,width=30)
# father_name.grid(row=7,column=1)

# zipcode=Entry(root,width=30)
# zipcode.grid(row=8,column=1)

# #Creating Save button.

# root.mainloop()

    

