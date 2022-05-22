"""
#1.Write a Python function to multiply all the numbers in a list.
#Sample list = [8,2,3,-1,7]
def multiply(mylist):
    result=1
    for x in mylist:
        result=result*x
    print(result)
mylist=[8,2,3,-1,7]
print(multiply(mylist))
"""


"""
#2.Write a Python function to sum all the numbers in a list.
#Sample list : [8, 2, 3, 0, 7]
def add(myList):
    sum=0
    for x in myList:
        sum=sum+x
    print(sum)
myList=[8, 2, 3, 0, 7]
print(add(myList))
"""

#3.Write a python function to find min of three numbers.(no parameter and no return type)









"""
#4.Write a function called fizz_buzz that takes a number.
#If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number.
def fizz_buzz(x):
    if x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    elif x%3==0 and x%5==0:
        print("FizzBuzz")
    else:
        print(x)
x=int(input("Enter the number."))
fizz_buzz(x)
"""


"""
#5.Create a function that can accept two arguments name and age and print its value.
def new(a,b):
    print(f"The name is {a} \nThe age is {b}")
new("Ujjwal",18)
"""

'''
#6.Write a program function to find max of three numbers.(no parameter and no return type)

def program():
    a=10
    b=20
    c=30
    if a>b and b>c:
        print(a)
    elif b>c and c>a:
        print(b)
    elif c>b and b>c:
        print(c)
print(program())
'''


'''
#7.Write a Python function to print the even numbers from a given list. 
#sample: [1,2,3,4,5,6]

def even(list):
    evennumber = []
    for i in list:
        if i%2==0:
            evennumber.append(i)
    return evennumber
list=[1,2,3,4,5,6]
print(even(list))
'''


'''
"""8.Write a Python function to print the odd numbers from a given list. 
sample: [1,2,3,4,5,6]"""

def odd(list):
    oddnumber=[]
    for i in list:
        if i%2!=0:
            oddnumber.append(i)
    return oddnumber
list=[1,2,3,4,5,6]
print(odd(list))
'''


'''
#9.Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime(number):
    if number%3==0 and number%9==0:
        return "composite number"
    else:
        return "prime number"
number=int(input("Enter a number: "))
print(prime(number))
'''

'''
#10. Write a function to reverse a string.
def reverse(x):
    str=""
    for i in x:
        str=i+str
    return str
'''



'''
#11.Write a program to create a function that takes two arguments, name and age, and print their value.
def info(name,age):
    print(f"My name is {name} and I am {age} y/o")
info("Ujjwal",18)
'''


'''
"""18. Define a function that accepts a number and returns whether the number is even or odd."""
def num(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
x=int(input("enter a number: "))
print(num(x))
'''


#22.Define a function that accepts radius and returns the area of a circle.
def circle(radius):
    return 13.4*radius**2
radius=int(input("enter a number: "))
print(circle(radius))




