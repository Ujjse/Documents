#Write a python program to print a multiplication table of any number using while loop. 

no=int(input("Enter any number: "))
i=1
while(i<=10):
	print(f"{no}*{i} = {no*i}")
	i=i+1