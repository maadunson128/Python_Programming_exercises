###Program: Average of numbers using sentinel loop

def main()->None:

    count:int = 0
    total:float = 0.0
    x = input("Enter a number (<Enter> to quit): ")

    while x != "":
        x = float(x)
        total += x
        count += 1
        x = input("Enter a number: (<Enter> to quit): ")

    try:
        print(f"Average of numbers: {total/count}")
    except ZeroDivisionError:
        print("Enter numbers to calculate the average.")

main()
