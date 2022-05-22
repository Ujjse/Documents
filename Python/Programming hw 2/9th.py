#Take input of age of 3 people by user and determine oldest and youngest among them.
Age_1=int(input("Enter the age of 1st person: "))
Age_2=int(input("Enter the age of 2nd person: "))
Age_3=int(input("Enter the age of 3rd person: "))
if Age_1<Age_2 and Age_2<Age_3:
    print(f"The youngest is {Age_1} years old")
elif Age_2<Age_3 and Age_3<Age_1:
    print(f"The youngest is {Age_2}")
elif Age_3<Age_2 and Age_2<Age_1:
    print(f"The youngest age is {Age_3}")
else:
    print("Equal Ages/Error")

if Age_1>Age_2 and Age_2>Age_3:
    print(f"The oldest is {Age_1}")
elif Age_2>Age_3 and Age_3>Age_1:
    print(f"The oldest is {Age_2}")
elif Age_3>Age_2 and Age_2>Age_1:
    print(f"The oldest is {Age_3}")
else:
    print("Equal Ages/Error")