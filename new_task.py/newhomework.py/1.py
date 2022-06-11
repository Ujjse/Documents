#1. Write a Python program to get the smallest number from a list.
#Step one.
'''
a=[1,2,3,4,5]
print(min(a))
'''

#2.  Write a Python function to check a list is empty or not.




#3.  Write a Python program to select an item randomly from a list.
'''
import random
list1=[1,2,3,4,5,6]
print(random.choice(list1))'''


#4.  Write a Python program to copy a list.
'''
a=["ujjwal",25,"ram"]
b=[]
b=a.copy()
print(a)
print(b)'''

#5.  Write a Python program to find the 2nd largest number in a list.
'''
a=[65,98,34,54,550,70,43]
a.sort()
print(a)
print("The second largest number is", a[-2])'''

#6.  Write a Python program to print a specified list after removing the 3rd elements.
'''
a=["ujjwal",25,"ram"]
print(a)
a.remove("ram")
print(a)'''
"""
#7. Write a Python program to count the number of even and odd numbers from a series of numbers.
from tkinter import Tk


data=[2,3,4,5,6,7,8,9,10]
a=0
b=0
for i in data:
    print(i)
if i%2==0:
    print


#8. Write a Python program to add an item in a tuple.
'''
a=("ujjwal",25,"ram")
print(a)
a.append(29)
print(a)'''

#9.  Write a Python program to convert tuple to list.
'''
a=("apple","banana","cherry")
print(a)
print(list(a))'''


#10.  Write a Python program to convert a tuple to a string.


#11.  Write a Python program to convert a list to a tuple.
'''
a=["apple","banana","cherry"]
print(a)
print(tuple(a))'''

#12.  Write a Python Program to Convert List of Tuple into Dictionary
'''
a=(1,"apple"),(2,"banana")
print(a)
print(dict(a))'''


#13.  Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
'''
a={0:1,1:20}
print(a)
a[2]=30
print(a)
'''

#14. Write a Python script to concatenate following dictionaries to create a new one. XXXXXXXX
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
print(dic1)
dic1.update(dic3)
print(dic1)
'''
#15.  Write a Python script to check if a given key already exists in a dictionary.
'''
data={"name":"Ujjwal","age":18}
if "name" in data:
    print("Present")
else:
    print("Absent")
'''

#16. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""
#a={5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
#print(a)
"""

#17. Write a Python script to merge two Python dictionaries.
'''
a={101:"Ujjwal",102:"Seetal"}
b={103:"Ujjeli",104:"Seeteli"}
a.update(b)
print(a)
'''
#18. Write a Python program to find the 3nd largest number in a list.
'''
a=[7,4,5,6,3,2,1]
a.sort()
print(a)
print(a[-3])
'''

#19. Write a Python program to create a set.
'''
a={1,2,3,4,5}
print(type(a))
'''

#20. Write a Python program to iteration over sets.





#21. Write a Python program to add member(s) in a set.
'''
a={1,3,4,5,6,2,7,9,8}
a.add(10)
print(a)
'''

#22.Write a Python program to remove item(s) from set.

a={1,3,4,5,2,7,6}
a.remove(3)
a.remove(5)
print(a)


#23. Write a Python program to remove an item from a set if it is present in the set.

a={1,2,3,4}
if 3 in a:
    print("Present")
else:
    print("Not available.")
a.remove(3)


#24. Write a Python program to create an intersection of sets. 

a={1,2,3,4}
b={2,3,5,6}
c=a.intersection(b)
print(c)


#25. Write a Python script to check if a given key exists in a dictionary.


data={101:"Ujjwal",102:"Seeteli",103:"Hari",104:10}
if 101 in data:
    print("Key Exists")
else:
    print("Key Does not exists.")


#26. Write a Python script to check if a given values exists in a dictionary.

data={101:"Seetal",102:"Ujjwal"}
y=input("Enter: ")
if y in data.values():
    print("Exists.")
else:
    print("Does not exists.")
"""


from tkinter import *
win=Tk()
win.title("System")
win.iconbitmap("/Users/ujjwalpariyar/Documents/new_task.py/newhomework.py/ujj.ico")
win.maxsize(width=300,height=200)
win.mainloop()