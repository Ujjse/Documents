#Write a program to accept two numbers and mathematical operators and perform operation accordingly.
number_1=int(input("Enter the first number: "))
number_2=int(input("Enter the second number: "))
operator=input("Enter any operator: ")
if operator=="+":
    print(number_1+number_2)
elif operator=="-":
    print(number_1-number_2)
elif operator=="*":
    print(number_1*number_2)
elif operator=="/":
    print(number_1/number_2)
elif operator=="%":
    print(number_1%number_2)
else:
    print("Invalid operator")