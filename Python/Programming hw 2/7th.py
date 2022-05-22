#Write a Python Program to Check Prime Number.
a=int(input("Enter a number: "))
if a<=1:
    print("It is composite number.")
    quit()

for b in range(2,a):
        if a%b==0:
            print("It is composite number.")
            quit()
else:
    print("It is prime number")
