#Program: Future Value in bank for n years

def main():
    amount = eval(input("Enter the amount to be deposited: "))
    interest = eval(input("Enter the interest rate(%): ")) / 100
    years = eval(input("Enter the number of years: "))

    for year in range(years):
        amount = amount * (1 + interest)

    print("The future value after ", years, 'years: ', amount)

main()