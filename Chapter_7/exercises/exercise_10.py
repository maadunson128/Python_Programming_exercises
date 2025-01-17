###Program: Finding the easter for years 1900 - 2099

'''The formula for Easter in the previous problem works for every year in
the range 1900-2099 except for 1954, 1981, 2049, and 2076. For these
4 years it produces a date that is one week too late. Modify the above
program to work for the entire range 1900-2099.'''


#function for finding easter
def find_easter(year)->int:
    #finding the values of a,b,c,d,e for easter date finding
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7
    return d+e

def main()->None:

    #input from the user -> year from 1982 to 2048
    year:int = int(input("Enter the year between 1900 to 2099(inclusive): "))

    #exception years
    exc_years:list[int] = [1954, 1981, 2049, 2076]
    
    #checking the year range
    if year < 1900 or year > 2099:
        print(f"Please, Enter a year between 1900 and 2099(inclusive).")
    else:
        value:int = find_easter(year)
        
        #handling the case is in the expection four years
        if year in exc_years:
            value -= 7
            
        #handling the values greater than 9
        if value > 0 and value < 10:
            print(f"Date of easter for year {year}: March {22+value}")
        else:
            print(f"Date of easter for year {year}: April {(22+value)%31}")
        

main()
