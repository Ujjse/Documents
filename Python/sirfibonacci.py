def Fibo(n):

    if n==1:

        return 0

    elif n==2:

        return 1

    else:

        return Fibo(n-1) + Fibo(n-2)

numberOfTerms=int(input("Enter the number of terms to be printed in the series: "))
n=1

while n<=numberOfTerms:
    
    print(Fibo(n))
    n=n+1
