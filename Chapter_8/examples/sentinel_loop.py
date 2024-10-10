##Sentinel loop
#Program: Averaging number

def main()->None:

    count:int = 0
    total:float = 0.0
    x:float = float(input("Enter a number (negative to exit): "))

    while x>=0:
        total += x
        count += 1
        x = float(input("Enter a number (negative to exit): "))

    print(f"Average of numbers: {total/count}")


main()
