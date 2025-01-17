###Program: Double amount time finder

##Note: I assumed that the initial amount is not interested compounded.

#function to finds the number of years
def find_time(amount, rate)->int:
    count:int = 0
    f_amount:float = 0
    
    while True:
        count += 1
        f_amount += amount * rate
        if amount + f_amount >= 2*amount:
            break

    return count


def main()->None:
    initial_amount:float = float(input("Enter the initial amount ($): "))
    rate:float = float(input("Enter the interest rate in %: "))

    print(f"The no of years the amount ${initial_amount} take to double: {find_time(initial_amount, rate/100)}years")


main()
