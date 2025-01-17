###Program: GCD(Greatest Common Divisor) of two numbers using Euclid's algorithm


#function to find gcd
def find_gcd(n:int, m:int)->int:

    #euclid's algorithm for GCD
    while True:
        n, m = m, n%m
        if m == 0:
            break

    return n


    
def main()->None:
    #user input: two integer numbers
    num1:int = int(input("Enter number 1: "))
    num2:int = int(input("Enter number 2: "))

    #finding GCD
    gcd:int = find_gcd(num1, num2)

    print(f"GCD of numbers {num1}, {num2}: {gcd}")

main()
