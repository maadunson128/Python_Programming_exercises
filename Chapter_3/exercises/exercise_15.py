# Program: To subract the sum of series from value of pi
import math
n = int(input("Enter the 'n' for finding the sum of series upto n terms: "))

def answer(n):
    sum = 0.0
    for i in range(n):
        term = (-1) **i * (4 / (2 * i + 1))
        sum = sum + term
    print(f"The final value after the subracting the sum of terms from pi: {math.pi - sum}")

answer(n)