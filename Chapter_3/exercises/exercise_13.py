#Program: To sum the series of numbers 


def find_sum(n):
    sum_numbers = 0
    for _ in range(n): 
        num = int(input("Enter the number: "))
        sum_numbers = sum_numbers + num

    print(f"The sum of {n} numbers you entered: {sum_numbers}")


n = int(input("Enter the 'n' (number of numbers to be summed): "))
find_sum(n)