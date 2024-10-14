###Program: Syracuse sequence

#Function to find the syracuse sequence
def syracuse_sequence(n)->None:
    num:int = n
    seq:list[int] = []
    
    while True:
        seq.append(num)
        
        if num%2 == 0:
            num = num//2
        else:
            num = 3*num + 1

        if num == 1:
            seq.append(num)
            break

    print(*seq, sep=',', end=".")
            

def main()->None:

    #user input number
    n:int = int(input("Enter a number: "))

    #finding the syracuse sequence
    syracuse_sequence(n)


main()
