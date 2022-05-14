print("Only valid weights are allowed for paragliding.\nEnter your weight to check if you are allowed or not. ")
weight=int(input("Enter your weight: "))
if weight<=50:
    print("Under weight for paragliding")
elif weight>50 and weight<150:
    print("Ok for paragliding")
else:
    print("Over weight")