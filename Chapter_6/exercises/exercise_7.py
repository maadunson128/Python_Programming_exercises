###Program: Nth fibonacci number

#function to calculate the nth fibonaaci number
def Nth_fibonacci(n:int)->int:
    first = 0
    second = 1
    #change the parameter according to if 0 is first fibonacci number.
    #parameter -> n-1 if 0 is first fibonacci number
    #else parameter -> n if 1 is forst fibonacci number
    for i in range(n): 
        next_no = first + second
        first = second
        second = next_no

    return first


def main()->None:

    #input from user
    n:int = int(input("n is nth fibonacci number. \nEnter the value of n: "))

    #calculating the nth fibonacci number
    number = Nth_fibonacci(n)

    print(f"The {n}th fibonacci number: {number}")


main()
        
