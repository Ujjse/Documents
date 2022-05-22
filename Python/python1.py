def function(percentage):
    percentage=(a+b+c)/3
    return percentage

a,b,c=input('enter scores of three subjects:').split()
a=int(a)
b=int(b)
c=int(c)
percentage=(a+b+c)/3
print('You got',percentage,'%')
if percentage>=90:
    print('GPA A')
elif(percentage>=70 and percentage<=90):
    print('GPA A-')
elif(percentage>=70 and percentage<80):
    print('GPA B')
elif(percentage>=60 and percentage<70):
    print('GPA C')
else:
    print('Better luck next time.')

