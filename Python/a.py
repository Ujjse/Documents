import pdb
bike1="yamaha"
bike1_price= 25000

bike2="honda"
bike2_price= 50000

pdb.set_trace()
name=input("Enter your name: ")
choose=int(input("Press 1 for yamaha and 2 for honda: "))
print(f"hello {name}")

if choose==1:
    print(f"{bike1} will cost you {bike1_price}")
elif choose==2:
    print(f"{bike2} will cost you {bike2_price+2000}")
else:
    print("press only 1 and 2")