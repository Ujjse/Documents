#8. Write a program to print the factorial of a number accepted from user.
num=int(input("Enter any number:"))
facto=0
i=1
while(i<=num):
    facto=num*i
    num=num-i
    print(facto)