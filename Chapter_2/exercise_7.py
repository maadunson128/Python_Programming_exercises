#Program: Total accumulation after n years

def main():
    amount = eval(input("Enter the amount to be invested for each year: "))
    interest = eval(input("Enter the interest rate: ")) /100
    years = eval(input("Enter the number of years: "))

    acc_amount = 0

    for year in range(years):
        acc_amount += amount
        acc_amount += acc_amount * interest
    print("The accumulated amount after ", years, ' years: ', acc_amount)    

main()  