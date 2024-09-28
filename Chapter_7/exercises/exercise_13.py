###Program: Finding the number of the day

'''The days of the year are often numbered from 1 through 365 (or 366).
This number can be computed in three steps using int arithmetic:
(a) dayNum = 3 1(month - 1) + day
(b) if the month is after February subtract (4(month) + 23)/ /10
(c) if it's a leap year and after February 29, add 1
Write a program that accepts a date as month/ day /year, verifies that it is a
valid date (see previous problem), and then calculates the corresponding
day number.'''

from exercise_12 import check_valid
from exercise_11 import check_leap

#function for giving the day number in the year.
def day_num(day, month, year)->int:
    
    #conditions given in question to find the Number of the day
    dayNum:int = 31 * (month - 1) + day
    if month > 2:
        dayNum -= ((4*month + 23) // 10)
    if check_leap(year) and month > 2:
        dayNum += 1

    return dayNum



def main()->None:

    #user input date -> date
    date:str = input("Enter the date (mm/dd/yyyy): ")
    date_mod:list[str] = date.split('/')

    #finding day, month, and year
    day:int = int(date_mod[1])
    month:int = int(date_mod[0])
    year:int = int(date_mod[2])

    if check_valid(day, month, year) == 'Valid':
        print(f"The number of the date {date}: {day_num(day, month, year)}")
    elif check_valid(day, month, year) == 'Not valid':
        print(f"Please enter a valid date.")

    
main()
    
            
