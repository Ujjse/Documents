"""
import math 
a=9
print(math.floor(a))
print(math.ceil(a))
print(math.fabs(a))
print(math.factorial(a))
print(math.sqrt(a))
print(math.pow(a,2))
"""

"""
import random
list=[1,2,3,4,5,6,7]
print(random.choice(list))
list3=("R","P","S")
print(random.choice(list3))


list2=random.randint(0,20)
print("Random number between 0 and 20 is % s" % (list2))


#This Shuffles the code.
sample=[1,2,3,4,5,6,7]
random.shuffle(sample)
print(sample)
"""

"""
import random
for i in range(50):
    print(random.randint(20,50))
"""

"""
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%Y"))

import datetime
x=datetime.datetime(2022,5,22)
print(x)
"""

"""
import random
a=[]
n=random.randint(1,20)
for i in range(1,n):
    a.append(i)
print(a)
"""

"""
import random
a=[]
for n in range(20):
    n=random.randint()
a.append(n)
print(a)
"""
""""
import random
print("Welcome to Rock papper and scissor game.\n Choose\n R for Rock.\n P for Papper.\n S for scissor")
list3=("R","P","S")
user=input("Enter your choice: ")
print(f"The comnputer chosed " + (random.choice(list3)))
if user==random.choice:
    print("Draw")
elif random.choice=="R" and user=="P" or random.choice=="P" and user=="S" or random.choice=="S" and user=="R":
    print("You win.")
elif random.choice=="P" and user=="S":
    print("You win.")
elif random.choice=="S" and user=="R":
    print("You win.")
else:
    print("You loose.")

"""

"""
data=[1,2,3,4,5]
for i in data:
    print(i)

data=list(range(20,30,1))
print(data)

data=["sunil","roshan",9]
print(data)
data.append(9)
data.append("Programming")
print(data)


data=["sunil","roshan",9]
print(data)
data.insert(2,"battle")



#updating data files
data=["sunil","roshan",9]
print(data)
data[0]=2
data[1]=0
data[2]="hari"
print(data)


data=["sunil","roshan",9]
print(data)
del data[1]
print(data)


data=["sunil","roshan",9]
print(data)
data.remove(9)
print(data)


data=["sunil","roshan",9]
print(data)
data2=[1,"a"]
print(data+data2)
data.pop
print(data)


data=["sunil","roshan",9]
data2=[]
data2=data.copy()
print(data2)
#######

data=("sunil","hello",9,["Sunil","hi",29])
print(data)
print(len(data))
data[3].pop()
print(data)
data[3].append("Master")
print(data)
data[3].remove("Sunil")
print(data)


######
print("Maximum is:",max(1,2,3,4,5,))
print("Minimum is:",min(1,2,3,4,5,))


#####
tuple1=("ram","shyam","hari")
print("Ujjwal",tuple1)
list1=list(tuple1)
print(list(tuple1))
list1.insert(3,"pops")
print("Changed list",list1)


#Adding the number in a set.
a={1,2,3,4,5,"Seetal"}
a.add(9)
print(a)
a.remove(2)
print(a)
a.discard(11)
print(a)
if "Seetal" in a:
    print("True")
else:
    print("False")



a={1,2,3,4,5,"Seetal"}
b={90,"Ujjwal"}
a.update(b)
print(a)

data1={1,2,3,4,4,5,5,6}
data2={1,2,45,5,65,56,4}
union_set= data1 | data2
print()


a={1,2,3,4}
b={5,6,7,8}
c=a.issubset(b)
print(c)

data={'name': "Sunil Rawat",'age':17}
print(data)
data1=dict(data={'name': "Sunil Rawat",'age':17})
print(data1)



#To access only on key and only values.
data={'name': "Sunil Rawat",'age':17}
print(data)
for i in data:
    print(i)
for i in data.values():
    print(i)
for i in data.items():
    print(i)
"""


"""

i=[1,2,3,4,5,6,7,8]
b=[]
sum=0
c=len(i)-1
while c>=0:
    sum=sum+i
    b.append(sum)
print(b)

"""

