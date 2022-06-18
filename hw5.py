"""
def adding(b):
    a=20
    return a+b
    print("Hi", sum)
sum=adding(10)
print(sum)
"""


"""
def add(x,y):
    c=x+y
    d=y-x
    return c,d
sum,sub=add(10,20)
print(sum)
print(sub)
"""




"""
def mul():
    a=10
    b=20
    total=a*b
    print(total)
mul()
"""


"""
def add(a,b):
    print (a+b)
add(5,6)
"""


"""
def greater(a,b,c):
    if a>=b and b>=c:
        return a
    elif b>=a and a>=c:
        return b
    elif c>=a and a>=b:
        return c
    else:
        return "hi"
a=int(input("Enter the number:"))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
print(greater(a,b,c))


def disp():
    def show():
        print("Hello world")
    print("World hwllo")
disp()
"""


'''
def reversed(x,y):
    def reversed(x,y):
        print(f"Hello{x},{y}")
    print(f"Hello world {x},{y}")
    reversed(100,12)
reversed(10,12)
####
y=10
def outer():
    z=4
    def inner():
        x=4
        print("x:",x)
        print("Inside the function y:",y)
    inner()
    print("z",z)
outer()
'''


'''
y=10
def outer():
    z=4
    def inner():
        nonlocal z
        x=4
        z=z+1
        print(x)
        print("Inside the function y",y)
        inner()
        print("z",z)
outer()
'''


"""
y=10
def inner():
    global y
    x=4
    print(x)
    print("Inside the function y",y)
print("y",y)
inner()
"""


"""
y=10
def inner():
    global y
    x=4
    y=y+1
    print(x)
    print("Inside the function y",y)
print("y",y)
inner()
"""


"""
a=10
def hello():
    a=12
    def hi():
        a=132
        print(a)
    hi()
hello()
"""


"""
def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner:",x)
    print("outer",x)
    inner()
    print("Outer:",x)
outer()
"""


"""
result=lambda n1,n2,n3:(n1+n2+n3, n1-n2-n3, n1*n2*n3, n1/n2/n3)
print("sum is",result(1,2,3)[0], "sub is",result(6,5,4)[1])
"""


"""
li=[5,7,22,97,54,62,23,73,61]
square_list=list(map(lambda x: x**2,li))
print(square_list)
"""

"""
a=[1,2,3]
b=[3,4,5]
abc=list(map(lambda x,y:x+y,a,b))
print(abc)
"""


"""
data=[1,2,3,4,5,5,6,6,7,9,10]
var=list(filter(lambda x: x%2==0, data))
print(var)
"""

'''
for i in range(0,3):
    a=input("Enter a number: ")
    if int(a)==123:
        print(True)
        break
    else:
        print(False)
'''

for i in range(0,3):
    username=input("Enter a username: ")
    password=input("Enter a password: ")
    print("Please confirm it again.")
    username1=input("Enter a username: ")
    password1=input("Enter a password: ")
    if username==username1 and password==password1:
        print("Succesfully saved.")
        break
    else:
        print("Datas dont match.")
print("Please Enter your username and password to log in.\n Welcome to foodmandu.\n")
id=input('Enter your email or username: ')
password2=input('ENter you password: ')
for i in range(0,3):
    if id==username and password2==password:
        print("Welcome to the page.")
        break
    else:
        print("Please enter it correctly.")
