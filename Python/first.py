def percentage(mark1,mark2,mark3):
	percent=(mark1+mark2+mark3)/3
	return percent
def GPA(percentage):
	if percentage>=90:
		gpa="GPA A"
	elif percentage<90 and percentage>=80:
		gpa="GPA A-"
	elif percentage<80 and percentage>=70:
		gpa="GPA B"
	elif percentage<70 and percentage>60:
		gpa="GPA A-"
	else:
		gpa="F"
	return gpa

print("Calculate percentage and GPA");
m1=int(input("Enter first mark:"))
m2=int(input("Enter second mark:"))
m3=int(input("Enter third mark:"))
percentageCalculated=percentage(m1,m2,m3)
print(str(percentageCalculated)+"%")
gpaCalculated=GPA(percentageCalculated)
print(gpaCalculated)