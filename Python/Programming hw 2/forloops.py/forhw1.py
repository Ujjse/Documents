'''
password_true=9823658272
for i in range(3,0,-1):
    password=int(input("Enter your password: "))
    if password == password_true:
        print("Correct Password")
        quit()
    else:
        print("Incorrect password")
print("Locked")
'''

'''
for i in range(1,6):
    print("Hello")



for i in range(0,5):
    print(f"Hello world {i}")


for i in range(1,6):
    print("Python")


for i in range(0,2):
    print("Learning Python")
   

st="Programming"
for i in st:
    print(i)



st=range(3)
for i in st:
    print(i)



hi= range(10,21)
for i in hi:
    print(i)


ujj=range(5,15,2)
for i in ujj:
    print(i)


st="Programming"
n=len(st)
for i in range (n):
    print(i, "=",st[i])


st="Programming"
for i in st:
    print(i)
else:
    print("Else Part")
    
'''
#No 1:
'''
percentage=int(input("Enter the percentage: "))
if percentage<40:
    print("Failed")
elif percentage>=40 and percentage<55:
    print("Fair")
elif percentage>=55 and percentage<65:
    print("Good")
elif percentage >=65:
    print("Excellent")
else:
    ("Please enter your percentage again")
'''

#No 2:
'''
a=10
b=20
c=a
a=b
print(c,a)
'''
#Qn 3
#Write a program to print multiplication table of a  number 10 using for loop.
'''
a=10

for i in range(1,11):
    print (a*i)

'''
#Qn 4
#Print list in reverse order using a loop. Hint: list1=[1,2,3,4]
'''
list1=[1,2,3,4]

'''

#Qn 5
#Display numbers from -10 to -1 using for loop.
'''
for i in range(-10,0):
    print(i)
'''

#QN 6
#Use else block to display a message “Done” after successful execution of for loop.
'''
num=int(input("Enter a number: "))
for num in range(0,1):
    if num==0 and num >2:
        print("Wow")
    else:
        print("done")
'''  

'''
#Qn 7
f=5
a=1
for i in range(5,0):
    a=i*a
    print(a)

'''