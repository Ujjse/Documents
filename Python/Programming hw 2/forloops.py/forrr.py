### For loop
# name = "Python"
# for i in name:
#     print(name)
#
# What is range function explain with example?


# a = "Python"
# for i in a:
#     print(a,end=" ")
#
# for  python in range(6):
#     print(a)


# for i in range(1, 52):
#     print(i)

# name = "Python"
# for i in name:
#     print(i)

# name = "Python"
# for ran in range(0,6):
#     print(ran,"=",name[ran])

# a = "Programming"
# for i in range(len(a)):
#     print(i, "=", a[i])
# else:
#     print("Python")

# num = 2
# for i in range(10, 0, -1):
#     print(f"{num} * {i} = {num * i}")

# a ="Python"
# for i in range(5,-1,-1 ):
#     print(a[i], end="")

# for i in range(5, -1, -1):
#     print(a[i], end="")


# Account Blocked:
# for i in range(2, -1, -1):
#
#     try:
#         password = int(input("Enter three digit PIN: "))
#         if password != 369: #Already saved pin
#             print(f"INVALID PIN.\nYou have {i} chance left.")
#             if i == 0:
#                 print("Multiple wrong PINS. \nYour account has been blocked. ")
#
#         else:
#             print("Welcome to IRON BANK")
#             break
#     except ValueError:
#      print("An exception occurs! \nMake sure PINs are in numbers.")
#      print(f"You have {i} chance left.")


## Making reverse of list
# list1 = [1, 2, 3]
# list2 = []
# for i in reversed(list1):
#     list2.append(i)
# print(list2)



# a = [5, 4, 8, 9, 10, 12]
# b = 0
# for i in a:
#     b = b + i
# print(b)

# import math
# a = [5, 4, 9, 8, 9]
# b = 1
# for i in a:
#     b = b * i
# print(b)


# def primeNumber(x):
#     if x > 1:
#
#         for i in range(2, int(x/2) + 1):
#             if x % i == 0:
#                 print(x, "is not prime number")
#                 break
#         else:
#             print(x, "is prime number")
#
#     else:
#         print(x, "is not a prime number")
#
# x = int(input("Enter number: "))
#
# primeNumber(x)

# star = "*"
# for i in range(5):
#     for x in range(5):
#         print(star, end="")
#     print(star)

# star = "*"
# for i in range(5):
#     for x in range(i):
#         print(star, end="")
#     print(star)
#

# star = "*"
# for i in range(5):
#     for j in range(5-i):
#         print(star, end="")
#     print(star) 