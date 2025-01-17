###Program: Finding prime number
import math

#Function to find prime number
def prime_number(n):
    
    ans = True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            ans = False

    if ans:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")



def main()->None:
    #user input: number n
    n = int(input("Enter a positive whole number after 2: "))

    #finding if it is prime number
    prime_number(n)


main()
