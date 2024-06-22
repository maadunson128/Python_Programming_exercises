# Program: To print the nth number in fibonacci series

def n_fibonacci(n):
    first = 0
    second = 1
    if n == 1:
        number = 1
    else:
        for i in range(n-1):
            number = first + second
            first = second
            second = number
    print(f"The {n}th fibonacci number: {number}")

n = int(input("Enter the value of n: "))

n_fibonacci(n)