#Write a program to check whether a number entered by user is even or odd.
number=int(input("Enter a number: "))
if number%2==0:
    print("It is even.")
elif number%2!=0:
    print("It is odd.")