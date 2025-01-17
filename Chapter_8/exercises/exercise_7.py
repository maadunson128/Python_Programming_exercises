###Program: Finding the two prime numbers for Goldbach conjecture

import math

#function to find the number is even and greater than 2 or not
def isEven(n)->bool:
    if n%2 == 0 and n > 2:
        return True
    return False

#function to find prime numbers list
def prime_list(n)->list[int]:
    prime:list[int] = []

    #creating the list of prime numbers
    for i in range(2, n):
        ans:bool = True
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                ans = False

        if ans:
            prime.append(i)

    return prime

#function to find two prime numbers
def find_two_prime(n, prime)->tuple[int, int]:

    for elem1 in prime:
        for elem2 in prime:
            if elem1 + elem2 == n: return elem1, elem2
        

def main()->None:
    
    #input from the user
    while True:
        n:int = int(input("Enter a even integer greater than 2: "))
        if isEven(n):
            break

    #creating a list of prime numbers for the given numbers
    prime = prime_list(n)


    #finding the two numbers that sum upto the given number
    num1, num2 = find_two_prime(n, prime)

    print(f"Two prime numbers that sum upto the given number: {num1}, {num2}")


main()
        

    
