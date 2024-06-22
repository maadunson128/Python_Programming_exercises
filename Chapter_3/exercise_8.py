#Program: To find epact

def find_epact(year):
    C = year // 100
    epact = (8 + (C//4)- C + ((80 + 13) // 25) + 11 * (year%19))%30
    print("Epact:", epact)

year = int(input("Enter the year to find the epact:"))
find_epact(year)