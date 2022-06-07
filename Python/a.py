def outer():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    sum=a+b
    def inner():
        return sum
    print(inner())
    return sum+5
print(outer())