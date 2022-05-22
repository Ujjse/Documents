#WAP which accepts marks of four subjects and display total marks, percentage and grade.

first=int(input("Enter the marks on your first subject: "))
second=int(input("Enter the marks of your second subject: "))
third=int(input("Enter the marks of your third subject: "))
fourth=int(input("Enter the marks of your fourth subject: "))

if first and second and third and fourth>100: #by this we can prevent errors of entering marks.
    print("Please enter your marks correctly and try again.")
    quit()
#using quit() will stop programme if marks inputed is more than 100.
Total_Marks=first+second+third+fourth
percentage=Total_Marks/4
if percentage>70:
    print("You scored Distinction")
elif percentage>60:
    print("You scored First Division")
elif percentage>40:
    print("You are Pass")
else:
    print("You Failed")
print(f"Your total marks is {Total_Marks}")
if percentage>90:
    print("Your grade is A+.")
elif percentage>80:
    print("Your grade is A")
elif percentage>70:
    print("Your grade is B+")
elif percentage>60:
    print("Your grade is B")
elif percentage>50:
    print("Your grade is C+")
elif percentage>40:
    print("Your grade is C")
else:
    print("Fail")

print("Total percentage is " + str(percentage) +"%")