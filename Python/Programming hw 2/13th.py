#Write a program to display "Hello" if a number entered by user is a multiple of five,otherwise print "Bye".
number=int(input("Enter a number: "))
if number%5==0:
    print("Hello")
else:
    print("Bye")