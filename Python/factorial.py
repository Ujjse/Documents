def factorial(n):
    if(n==1):
        result=1
    else:
        result=n*factorial(n-1)
    return result

x=int(input("please input a number to calculate the factorial"))
result=factorial(x)
print(result)