#This file is used for exercise 7


for i in range(60):
   temp =  i / 60
   temp *= 60
   print(f"{i, temp}  {i == round(temp, 2)}")

