#############################################################################
# Question 1.
# Write a Python function to multiply all the numbers in a list. Sample list = [8,2,3,-1,7]
#############################################################################

# def product():
#     list1 = [8, 2, 3, -1, 7]
#     value = 1
#     while list1 != []: #using while loop
#         pops = list1.pop()
#         value = value * pops
#     print(f"The multiplication of list {[8, 2, 3, -1, 7]} is {value}")
#
# product()


# Method 2

# def product():
#     list1 =  [8, 2, 3, -1, 7]
#     value =  1
#     for i in list1: # Using for loop
#         value = value * i
#     print(f"The multiplicatio of {list1} is {value}")
#
# product()


#############################################################################
# Question 2
# Write a Python function to sum all the numbers in a list. sample list = [8, 2, 3, -1, 7]
#############################################################################

# Method 1
# def method1():
#     import math
#     list1 = [8, 2, 3, -1, 7]
#     print(f"The sum is {int(math.fsum(list1))}")
# method1()
#
# # Method 2 using for loop
# def method2():
#     list1 = [8, 2, 3, -1, 7]
#     value = 0
#     for i in list1:
#         value = value + i
#     print(f"The sum of the list1 is {value}")
# method2()

# Method 3 using while loop
# def method3():
#     list1 = [8, 2, 3, -1, 7]
#     value = 0
#     while list1 != []:
#         pops = list1.pop()
#         value = value + pops
#     print(f"The sum of list1 is {value}")
#
# method3()

# method 4
# print(sum([8, 2, 3, -1, 7]))


# Method 5

#############################################################################
# Question 3
# Write a python function to find min of three numbers.(no parameter and no return type)
#############################################################################

# def compare():
#     num1 = int(input("First Number: "))
#     num2 = int(input("Second Number: "))
#     num3 = int(input("Third number: "))
#     if num3 > num1 < num2:
#         print(num1, "is smaller")
#     elif num1 > num2 < num3:
#         print(num2, "is smaller")
#     else:
#         print(num3, "is smaller")
#
# compare()


#############################################################################
# Question 4
# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.
#############################################################################

# def fizz_buzz(x):
#    if x % 3 == 0:
#        if x % 5 == 0:
#            return "FizzBuzz"
#        return "Fizz"
#    elif x % 5 == 0:
#        return "Buzz"
#
# def main():
#     num = int(input("Enter number: "))
#     number = fizz_buzz(num)
#     print(number)
#
# if __name__ == '__main__':
#     main()


#############################################################################
# Question 5
# Create a function that can accept two arguments name and age and print its value.
#############################################################################

# def detail(name, age):
#     return f"Your name is {name} \nYou are {age}years old"
#
# def main():
#     name = input("What's your name?: ")
#     age = int(input("What's your age? "))
#     info = detail(name, age)
#     print(info)
#
# main()

#############################################################################
# Question 6
# Write a program function to find max of three numbers.(no parameter and no return type)
#############################################################################

# def compare():
#     num1 = int(input("First Number: "))
#     num2 = int(input("Second Number: "))
#     num3 = int(input("Third number: "))
#     if num3 < num1 > num2:
#         print(num1, "is greater")
#     elif num1 < num2 > num3:
#         print(num2, "is greater")
#     else:
#         print(num3, "is greater")
#
# compare()


#############################################################################
# Question 7.
#7. Write a Python function to print the even numbers from a given list. sample: [1,2,3,4,5,6]
#############################################################################

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = []
#
# # Method 1
# # Using for loop
# for i in list1[1::2]:
#     list2.append(i)
# print(f"Even numbers are {list2}")

# # Method 2
# # Using while loop
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = []
# while len(list1) != 3:
#     list2 = sorted(list1[1::2])
#     print(f"Even number are {list2}")
#     break


#############################################################################
# Question 8.
# Write a Python function to print the odd numbers from a given list. sample: [1,2,3,4,5,6]
############################################################################

# def sortodd():
#     list1 = [1, 2, 3, 4, 5, 6]
#     list2 = []
#     for i in list1[::2]:
#         list2.append(i)
#     print(f"Odd numbers are {list2}")
#
# sortodd()

#############################################################################
# Question 9.
# Write a Python function that takes a number as a parameter and check the number is prime or not.
#############################################################################

# def Primenumber(x):
#
#     if x > 1:
#         for i in range(2, int(x/2)+1):
#             if x % i == 0:
#                 return f"{x} is not prime number"
#         else:
#             return f"{x} is prime number."
#
#
#     else:
#         print(f"{x} is not prime number")
#
# num = int(input("Enter number to know prime number: "))
# print(Primenumber(num))


#############################################################################
# Question 10.
# Write a function to reverse a string.
#############################################################################

# Method 1
# language = "PYTHON"
# def reverse():
#     data = language[-1:-7:-1]
#     print(data)
# reverse()

# Method 2
# Using for loop
# language = "PYTHON"
# for i in reversed(language):
#     print(i, end="")


#############################################################################
#Question 11.
# Write a program to create a function that takes two arguments, name and age, and print their value.
#############################################################################

# def info(*args):
#     return f"Your name is {name} and age is {age}"
# name = input("Write your name: ")
# age = input("Write your age: ")
# print(info(name, age))


#############################################################################
# Question 12.
# Write a program to create function func1() to accept a variable length of arguments and print their value
#############################################################################

# def func1(*args):
#     print(f"The sum of {args[0]}, {args[1]}, {args[2]} is {args[0] + args[1] + args[2]}")
# func1(1, 2, 3, 4, 5, 6)


#############################################################################
# Question 13.
#Write a program to create function calculation() such that it can accept two variables and
# calculate addition and subtraction.Also, it must return both addition and subtraction in a single return call.
#############################################################################

# print("Note that subtraction will be done from num2 to num1")
# def calculation(x, y):
#     return f"The addition of {x} and {y} is {x + y}\nThe subtraction of {x} and {y} is  {x - y}"
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# calculate = calculation(num1, num2)
# print(calculate)
#


#############################################################################
# Question 14.
#14. Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
#############################################################################

# def show_employee(x, y= 9000):
#     print("Hello", x)
#     print("Your salary is ", y)
#
# show_employee("Sujan")
# show_employee("Sujan", 150000)


#############################################################################
#Question 15.
# Find the largest item from a given list. sample: [4, 6, 8, 24, 12, 2]
#############################################################################

# sample = [4, 6, 8, 24, 12, 2]
# sample.sort()
# largest = sample.pop()
# print(f"The largest in the [4, 6, 8, 24, 12, 2] is {largest}")


#############################################################################
# Question 16.
# Find the smallest item from a given list. sample: [4, 6, 8, 24, 12, 2]
#############################################################################

# list1 = [4, 6, 8, 24, 12, 2]
# list1.sort()
# list2 = list1.pop(0)
# print("The smallest of [4, 6, 8, 24, 12, 2] is {list2}".format(list2= list2))


#############################################################################
# Question 17.
# Define a function that accepts roll number and returns whether the student is present or absent.
#############################################################################

# import random
# def Student(rolls):
#      students = {
#         1 : "Sujan",
#         2 : "Midas",
#         3 :"Libon",
#         4 : "Ujjwal",
#         5 : "Safal",
#         6 : "Alekh"
#      }
#      comp = random.randrange(1, 8)
#      print("Present students are: ")
#      if comp != rolls:
#         for i in students:
#             if i == comp:
#                 continue
#             print(students[i])
#      absent = f"Roll no.{comp} is absent : [{students[comp]}]"
#      print(absent)
#
#
# roll_range = input("Enter students roll range from 1 to 7: ")
# Student(roll_range)


#############################################################################
#Question 18.
# Define a function that accepts a number and returns whether the number is even or odd.
#############################################################################

# def nature(x):
#     if x % 2 == 0:
#         return f"{x} is even"
#     else:
#         return f"{x} is odd"
#
# def main():
#     number = int(input("Enter a number: "))
#     even_odd = nature(number)
#     print(even_odd)
#
# if __name__ == '__main__':
#     main()
#


#############################################################################
# Question 19.
#Define a function which counts vowels and consonant in a word.
#############################################################################

#Python program to count vowel or consonant of the given string

# text = input("Write as you like: ").strip().lower()
#
#
#
# def count(vowels):
#     vow = 0
#     cons = 0
#     for vowel in text:
#         match vowel:
#             case "a" | "e" | "i" | "o" | "u":
#                 vow += 1
#             case _:
#                 cons += 1
#
#     print(f"The number of vowels are: {vow}")
#     print(f"The number of consonents are {cons}")
#
# count(text)

#############################################################################
#Question 20.
# Define a function that returns Factorial of a number.
#############################################################################

# def Factorial(x):
#     value = 1
#     for i in range(1, int(x + 1)):
#         value = value * i
#     print(f"The factorial of {x} is {value}")
#
# num = int(input("Enter a number whose factorial is needed: "))
# Factorial(num)



#############################################################################
# Question 21.
# Define a function that accepts lowercase words and returns uppercase words
#############################################################################

# text = input("Write a paragraph in lowercase: ")
#
# def upper(up):
#     if up == up.lower():
#         print(up.upper())
#     else:
#         print(up.upper())
# upper(text)


#############################################################################
# Question 22.
# Define a function that accepts radius and returns the area of a circle.
#############################################################################
import math
def circle(radius):
   area = pow(radius, 2) * math.pi
   return f"The area of circle is {area.__round__(3)}cm²"

def main():
   r = int(input("Enter radius of a circle in cm: "))
   Area = circle(r)
   print(Area)

if __name__ == '__main__':
   main()