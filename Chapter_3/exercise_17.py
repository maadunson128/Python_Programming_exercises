#Program: Finding square root by own algorithm
import math
number = float(input("Enter the number to find square root: "))
iteration = int(input("Enter the value of n (number of times you want to improve the guess): "))

def find_square_root(number, iteration): 
    guess = number / 2
    for i in range(iteration):
        guess = (guess + (number / guess)) / 2

    final_value = guess
    return final_value


final_value = find_square_root(number, iteration)
print("The square root of", number, ":", final_value)
print("Difference between estimated and actual square root value of", number,":", math.sqrt(number) - final_value)