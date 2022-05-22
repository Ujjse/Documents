'''
#1. Create a function with variable length of arguments.
def new(a,b):
    print(a+b)
new(10,20)
'''


"""
#2. Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#At last, an outer function will add 5 into addition and return it.

def outer():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    sum=a+b
    def inner():
        return sum
    print(inner())
    return sum+5
print(outer())
"""

"""
#3. Assign a different name to function and call it through the new name Below is the function 
#display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
def display_student(name, age):
    def show_tudent(name, age):
        print(f"The name is {name} and the age is {age}.")
    show_tudent("ujjwal",18)
display_student()
"""
"""
#4. Find the largest item from a given list.
x=[1,2,3,4,5,6,7,8]
print(max(x))

#5. What is the difference between 10 / 3 and 10 // 3?
#Ans:10/3 is just a divide operator where as the 10//3 is the floor division operator.
a=10/3
b=10//3
print(a,b)

#6. What about two asterisks (**)?
#Ans:It helps to find the square root or the exponent of a number.
a=5**2
print(a)

#7.What is the difference between local and global variables?
#The variable that lies outside a function is a global variable and the variable that lies inside a function
#is known as local variable.
a=10 #This a is a global variable.
def sum():
    b=20#This b is a local variable
    return a+b
print(sum())


#8. Write a function called fizz_buzz that takes a number.If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number.
def fizz_buzz():
    a=int(input('Enter a number: '))
    if a%3==0 and a%5==0:
        print("fizzbuzz")
    elif a%3==0:
        print("Fizz")
    elif(a%5==0):
        print("buzz")
    else:
        print(a)
print(fizz_buzz())
"""
"""
#9. Write a function for checking the speed of drivers. If speed is less than 70, it should print “Ok”.
#if the speed is 80, it should print: “Warning”.
def speed():
    x=int(input("Enter the speed: "))
    if x<=70:
        print("OK")
    elif x>=80:
        print("Warning")
    else:
        print("Welcome to heaven.")
print(speed())


#10. Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number. 
a=int(input("enter a number: "))
for i in range(1,11):
    sum=a*i
    print(sum)

"""
"""
#11. Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.
a=int(input('Enter a number: '))
print(reversed(int(a)))


"""
"""
#12. Write a python program that return the number of characters in a string. 
#myList = "Parameter"
myList="Parameter"
length=len(myList)
print(length)

#13. Write a Python program to multiply all the numbers in a list using while and for loop.
Sample_list = [8,2,3,-1,7]
def product():
    list1 = [8, 2, 3, -1, 7]    
    value = 1
    while list1 != []:
        pops = list1.pop()
        value = value * pops
    print(f"The multiplication of list {[8, 2, 3, -1, 7]} is {value}")
product()
"""

#14. Write a Python program to sum all the numbers in a list using for loop and while loop.Sample_list=[8, 2, 3, 0, 7]
a=[8,2,3,0,7]
sum=0
i=0
lists=len(a)
while(i<lists):
    sum=sum+a[i]
    i=i+1
print(sum)

a = [8,2,3,0,7]
b = 0
for i in a:
    b = b + i
print(b)

"""17. Sum : 1 to 10 (or any number) using while loop.
"""

sum=0
i=0
while i<=10:
    sum=sum+i 
    i=i+1
print(sum)


"""18. Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""

def even(list):
    evennumber = []
    for i in list:
        if i%2==0:
            evennumber.append(i)
    return evennumber
list=[1,2,3,4,5,6,7,8,9]
print(even(list))

"""19. Write a Python program to print the odd numbers from a given list. 
Sample List : [12,13,14,15,16,17,18,19]"""

def odd(list):
    oddnumber = []
    for i in list:
        if i%2!=0:
            oddnumber.append(i)
    return oddnumber
list=[1,2,3,4,5,6,7,8,9]
print(odd(list))

"""20. Write a program to accept percentage and display the Category according to the  following criteria :
Percentage	Category
< 41	                     Failed
=41 & <55	Fair
=55 & <65	Good
=65	                     Excellent"""


marks=int(input("Enter your marks: "))
if marks>=65:
    print("Excellent")
elif  marks>=55 and marks<65:
    print("Good")
elif  marks>=41 and marks<55:
    print("Fair")
else:
    print("Failed")