#Write a program to check whether a person is eligible for voting or not. (accept age from user)
print("Enter your age to find if you are eligible for voting or not.")
Age=int(input("Enter the age: "))
if Age<18:
    print("Not eligible")
elif Age>18:
    print("Eligible")
else:
    print("Please enter it correctly.")