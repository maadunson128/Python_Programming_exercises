###Program: Average of numbers using sentil loop

def main()->None:

    filename = input("Enter the filename: ")
    infile = open(filename, 'r')
    x = infile.readline().strip()
    total:float = 0.0
    count:int = 0
    
    while x != "":
        total += float(x)
        count += 1
        x = infile.readline().strip()

    print(f"Average of numbers: {total/count}")


main()
