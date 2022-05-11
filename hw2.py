print(" Choose the operators. ")
print(" 1 for Adiition. ")
print(" 2 for substraction. ")
operator=int(input("Enter the operator you want: "))
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if operator==1:
    print(a+b)
elif operator==2:
    print(a-b)
else:
    print("Please try again.")