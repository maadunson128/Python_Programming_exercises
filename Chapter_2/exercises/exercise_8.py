#Program: Total future value using interest for periods

def main():
    amount = eval(input("Enter the amount to be invested: "))
    interest = eval(input("Enter the yearly nominal interest rate: ")) / 100
    period_year = eval(input("Enter the number of times the interest calculated for each year: "))
    years = eval(input("Enter the total number of years: "))
    interest_period = interest / period_year
    periods = years * period_year

    for i in range(periods):
        amount = amount * (1 + interest_period)
    
    print("The accumulated amount after", years, 'years: ' , amount)

main()

#This gives the same result like the interest calculated for each year.