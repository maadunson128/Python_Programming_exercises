#Program: To find average of numbers the user entered

n = int(input("Enter the number of numbers you are going to give: "))

def find_average(n):
    sum_numbers = 0
    for i in range(n):
        number = int(input(f"Enter the number {i+1}: "))
        sum_numbers = sum_numbers + number
        average = sum_numbers / n
    
    print(f"The average of {n} numbers you entered: {average}")

find_average(n)