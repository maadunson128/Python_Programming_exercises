###Program: Leap year or not

#function to check for leap year or not
def check_leap(year:int)->bool:
    ans:bool = False
    if year%400 == 0:
        ans = True
    elif year%100 == 0:
        ans = False
    elif year%4 == 0:
        ans = True

    return ans
    

def main()->None:

    #input from the user -> year
    year = int(input("Enter the year: "))

    #checking for leap year
    ans:bool = check_leap(year)

    print(f"Is year {year} a leap year: {ans}")

if __name__ == '__main__':
    main()
