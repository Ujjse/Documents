"""N students take K apples and distribute them among each other evenly. The remaining 
(the undivisible) part remains in the basket. How many apples will each single student 
get? How many apples will remain in the basket? The program reads the numbers N and 
K. It should print the two answers for the questions above."""



n=int(input("Enter the number of students: "))
k=int(input("Enter the num of apples: "))
#if we divide k by n we will find the apples distribuited.
apples_distribuited=int(k/n)
#By this we can find the equal amt of apples distribuited.
total_apples=int(n*apples_distribuited)
#if we subtract no of apples by distribuited apples we get remaining apples.
apples_in_basket=int(k-total_apples)
print(f"The total apples distribuited to each other is {apples_distribuited}")
print(f"The remaining apples is basket is {apples_in_basket}")