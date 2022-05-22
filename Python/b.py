"""A school decided to replace the desks in three classrooms. Each desk sits two students. 
Given the number of students in each class, print the smallest possible number of desks 
that can be purchased.
The program should read three integers: the number of students in each of the three 
classes, a, b and c respectively."""

a=int(input("enter the number of students:"))
b=int(input("enter the number of students :"))
c=int(input("enter the number of students: "))
noOfDeskIna=a/2
noOfDeskInb=b/2
noOfDeskInc=c/2
print(f"Number of desk required in a {noOfDeskIna}")
print(f"Nunber of desk required in b {noOfDeskInb}")
print(f"Number of desk required in c{noOfDeskInc}")
if a<b and b<c:
    print(noOfDeskIna)
elif b<c and c<a:
    print(noOfDeskInb)
elif c<b and b<a:
    print(noOfDeskInc)
else:
    print("Equal")