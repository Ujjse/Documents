"""A school decided to replace the desks in three classrooms. Each desk sits two students. 
Given the number of students in each class, print the smallest possible number of desks 
that can be purchased.
The program should read three integers: the number of students in each of the three 
classes, a, b and c respectively."""

a=int(input("Enter the no of students in a: "))
b=int(input("Enter the no of students in b: "))
c=int(input("Enter the no of students in c: "))
#Each desk= 2 students.
#so we divide no of students by 2.
#after that we can achieve the no of required desk.
desks_in_a=a/2
desks_in_b=b/2
desks_in_c=c/2
print(f"The no of desks required in a is {desks_in_a}")
print(f"The no of desks required in b is {desks_in_b}")
print(f"The no of desks required in c is {desks_in_c}")
#now as we achieved the no of desks required.
#now we can use the if function to find out the lowest possible desk.
if a<b and b<c:
    print(f"The smallest desk is {desks_in_a}")
elif b<c and c<a:
    print(f"The smallest desk is {desks_in_b}")
elif c<b and b<a:
    print(f"The smallest desk is {desks_in_c}")
else:
    print("Equal desks in all")