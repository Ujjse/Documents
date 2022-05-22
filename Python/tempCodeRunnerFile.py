#Write a Python Program to Check Prime Number.
a=int(input("Enter a number: "))
if a==1 and a==2:
    print("It is composite")
elif a%2==0 and a%9==0:
    print("It is composite")
else:
    print("It is prome")