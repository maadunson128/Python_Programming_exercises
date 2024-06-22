#Program: To find the sum of 'n' natural numbers

def find_sum(n):
    numbers = range(n+1)
    sum_numbers = sum(numbers)
    print(f"The sum of first {n} natural numbers: {sum_numbers}")

print("Note: The 'n' represents the number of first natural numbers to be summed.")
n = int(input("Enter the value of n: "))
find_sum(n)