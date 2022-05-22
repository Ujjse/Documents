"""Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where 
1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display an error message if the user enters a number
that is outside the range of 1 to 12."""
def month(x):
    if x==1:
        return " January "
    elif x==2:
        return " Fubruary "
    elif x==3:
        return " March "
    elif x==4:
        return " April "
    elif x==5:
        return " May "
    elif x==6:
        return " June "
    elif x==7:
        return " July"
    elif x==8:
        return " August "
    elif x==9:
        return " September "
    elif x==10:
        return " October "
    elif x==11:
        return " November "
    elif x==12:
        return "December "
    else:
        return " Error "
#Now we have to use the input function.
#then print it.
x=int(input("Enter the number of month you want to know: "))
print(month(x))