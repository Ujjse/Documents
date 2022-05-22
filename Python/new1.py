def percentage(mark1,mark2,mark3):
	percent=(mark1+mark2+mark3)/3
	return percent
def GPA(percentage):
	if percentage>=90:
		gpa="A"
	elif percentage<90 and percentage>=80:
		gpa="A-"
	elif percentage<80 and percentage>=70:
		gpa="B"
	elif percentage<70 and percentage>60:
		gpa="A-"
	else:
		gpa="F"
	return gpa

print(" Enter your marks to see your total percentage and GPA");
m1=int(input("Enter first mark:"))
m2=int(input("Enter second mark:"))
m3=int(input("Enter third mark:"))
percentageCalculated=percentage(m1,m2,m3)
print(str(percentageCalculated)+"%")
gpaCalculated=GPA(percentageCalculated)
print(gpaCalculated)