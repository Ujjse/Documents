def leapyear(x):
   if x%4==0:
      if x%100==0:
         if x%400==0:
            return"It is a leap year."
            
   if x%4==0:
      if x%100==0:
         if x%400>0:
            return"It is not a leap year"

   else:
      return"It is not a leap year"
x=int(input("Enter the year: "))
print(leapyear(x))
