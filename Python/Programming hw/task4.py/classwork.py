"""
def cw():
    print("Hello")
    print(5* " Python ")
print(cw())

def hi():
    a=10
    b=20
    c=a+b
    print(c)
print(hi())
"""
"""
def add(x):
    if (x%2==0):
        print ("It is even number.")
    else:
        print ("It is odd.")
x=int(input("Enter any number: "))        
print(add(x))
"""
"""
def call(username,email,contact_no,):
    print(f"The username is {username} and the email is {email} and the contact no is {contact_no}")

username=input("Enter the username")
email=input("enter the email")
contact_no=int(input("ENter the number"))
call(username,email,contact_no)
"""
"""
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
def calc():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)


"""
"""
def variable(first,second,third):
    if(first>second and second>third):
        print(f"First is greater{first}")
    elif(second>third and third>first):
        print(f"Second is greater{second}.")
    elif(third>first and first>second):
        print(f"Third is greater{third}")
        
variable(1,2,3)
"""


"""

a=[1,2,3,4]
sum=0
i=0
lists=len(a)
while(i<lists):
    sum=sum+a[i]
    i=i+1
print(sum)

def sum():

"""

"""
a=[1,2,3,4]
sum=1
i=0
lists=len(a)
while(i<lists):
    sum=sum*a[i]
    i=i+1
print(sum)
"""
"""
a=[1,2,3,4]
b=[]
count=len(a)-1
while count>=0:
    b.append(a[count])
    count-=1
    print(b)

"""
"""
def pw(x, y):
    z=x**y
    print(z)
pw(5, 2)
"""
"""
def show(name,age=20):
    print(name,age)
show(name="Sunil",age=39)
"""
"""
def show(*num):
    z=num[0]+num[1]+num[2]
    print(z)
show(5,4,3)
"""
def show(**num):
    z=num['a']+num['b']+num['c']
    print(z)
show(a=5,b=4,c=3)
