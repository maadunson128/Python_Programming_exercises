'''A formula for computing Easter in the years 1982-2048, inclusive, is as
follows: let a = year%19, b = year%4, c = year%7, d = (19a + 24)%30,
e = (2b + 4c + 6d + 5)%7. The date of Easter is March 22 + d + e (which could be in April). Write a program that inputs a year, verifies that it is in
the proper range, and then prints out the date of Easter that year.'''

###Program: Finding the easter for year


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
    year:int = int(input("Enter the year between 1982 to 2048: "))

    #checking the year range
    if year < 1982 or year > 2048:
        print(f"Please, Enter a year between 1982 and 2048.")
    else:
        value:int = find_easter(year)

        #handling the values greater than 9
        if value > 0 and value < 10:
            print(f"Date of easter for year {year}: March {22+value}")
        else:
            print(f"Date of easter for year {year}: April {(22+value)%31}")
        

main()
        
    
