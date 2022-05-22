print("Certain ages people can only give votes. \nEnter your age to check if your are eligible or not.")
age=int(input("Enter the age: "))
if age>=18:
    print("You are elligible.")
elif age<18:
    print("Not elligible.")
else:
    print("Please try again.")