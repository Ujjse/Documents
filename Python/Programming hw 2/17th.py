#Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
a=int(input("Enter a number: "))
if a%2==0 and a%3==0: #It helps to check if both are divisible by 2 And 3 or not.
    print("It is divisible by both 2 & 3.")
else:
    print("It is not divisible by both 2 and 3.")