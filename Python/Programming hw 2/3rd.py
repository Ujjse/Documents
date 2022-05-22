#Given three integers, print the smallest one. (Three integers should be user input)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
# we need the smallest so we used (<) sighn to compare the smallest.
if a<b and b<c:
    print(f"The smallest number is {a}")
elif b<a and a<c:
    print(f"The smallest number is {b}")
elif c<a and a<b:
    print(f"The smallest number is {c}")
else:
    print("Equal numbers")