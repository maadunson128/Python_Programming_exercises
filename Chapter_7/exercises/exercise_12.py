###Program: check if a date is valid or not

from exercise_11 import check_leap

#function to check the date is valid or not
def check_valid(day:int, month:int, year:int)->str:
    value:str = "Not valid"

    #checking if the month is between 1 and 12
    if month < 1 or month > 12:
        return value

    #checking the day is valid or not
    if day < 1 or day > 31:
        return value
    
    #checking for day is valid or not based on month and year(leap year and non leap year)
    if month in range(1, 12, 2):
        if day < 1 or day > 31:
            return value
    elif month in range(4, 13, 2):
        if day < 1 or day > 30:
            return value
    elif month == 2:
        if (check_leap(year)) and (day < 1 or day > 29):
            return value
        elif (check_leap(year) == False) and (day < 1 or day > 28):
            return value
    
    return "Valid"
        

def main()->None:

    #input from user -> date
    date:str = input("Enter the date (month/day/year): ")
    date_mod:list[str] = date.split('/')

    #finding day, month, and year
    day:int = int(date_mod[1])
    month:int = int(date_mod[0])
    year:int = int(date_mod[2])

    print(f"The date {date} is {check_valid(day, month, year)}.")

if __name__ == "__main__":
    main()

