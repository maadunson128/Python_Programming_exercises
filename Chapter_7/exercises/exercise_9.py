'''A formula for computing Easter in the years 1982-2048, inclusive, is as
follows: let a = year%19, b = year%4, c = year%7, d = (19a + 24)%30,
e = (2b + 4c + 6d + 5)%7. The date of Easter is March 22 + d + e (which could be in April). Write a program that inputs a year, verifies that it is in
the proper range, and then prints out the date of Easter that year.'''

###Program: Finding the easter for year
