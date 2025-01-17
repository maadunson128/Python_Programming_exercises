###Program: Fibonacci number


#function to find the fibonacci number
def find_fibonacci(n)->int:
    first:int = 0
    second:int = 1
    next_v:int = None
    #returns the first number
    if n == 1:return 1

    #adding second and first for next number
    for i in range(n-1):
        next_v = first + second
        first, second = second, next_v

    return next_v





def main()->None:
    #user input:n -> nth fibonacci number
    n:int = int(input("Enter the value of n: "))

    num:int = find_fibonacci(n)

    print(f"{n}th fibonacci number: {num}")


main()
