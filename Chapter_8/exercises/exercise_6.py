###Program: Prime numbers upto given number
import math

#Function to find prime numbers upto n number
def find_prime_numbers(n):
    print(f"Prime numbers between 2 and {n}: ")
    
    for i in range(2, n+1):
        ans:bool = True
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                ans = False

        if ans:
            print(i, end=" ")
        

def main()->None:
    #user input for n -> upper limit upto where prime numbers going to printed
    n = int(input("Enter the value of n (n>=2): "))

    find_prime_numbers(n)

main()
