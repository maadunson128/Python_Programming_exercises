#Program: Factorial program

n = int(input("Enter the value of n to calculate its factorial: "))

fact = 1
for factor in range(n, 1, -1):
    fact = fact * factor

print("Factorial of ", n,":", fact)
