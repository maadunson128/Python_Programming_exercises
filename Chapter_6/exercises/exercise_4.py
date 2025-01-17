###Program: sum and sum of cubes of N natural numbers

import math
#function to calculate the sum of n natural numbers
def sumN(n:int)->int:
    return sum(range(n))

#function to calculate the sum of cubes of n natural numbers
def sumNcubes(n:int)->int:
    cubes = [math.pow(x, 3) for x in range(n)]
    return int(sum(cubes))

def main()->None:
    #input from the user
    n = int(input("'n' means number of natural numbers. \nEnter the value of n: "))

    #calculating sum and sum of cubes of N natural numbers
    sum_n = sumN(n)
    sum_cubes_n = sumNcubes(n)

    print(f"The sum of {n} natural numbers: {sum_n} \nSum of cubes of {n} natural numbers: {sum_cubes_n}")


main()
    
    
