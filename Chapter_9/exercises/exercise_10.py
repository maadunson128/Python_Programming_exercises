###program: Pi approximation
from random import random
#function to give info about the simulation
def info()->None:
    print("This is simualation of throwing darts and finding the approximation of pi.")

#function to simulate the approximate value of pi
def simulatePi(n:int)->float:

    dart_hits:int = 0
    #simulation for approximate pi
    for _ in range(n):
        #random x, y co-ordinates for 2X2 square cabinet
        x_coord:float = 2*random() - 1 
        y_coord:float = 2 * random() - 1

        if (x_coord ** 2) + (y_coord **2) <= 1:
            dart_hits += 1

    return 4 * (dart_hits / n)


def main()->None:
    #info about the simulation
    info()

    #getting inputs
    n:int = int(input("Enter the number of darts to throw: "))

    #simualating to get approximate value of pi
    pi_value:float = simulatePi(n)

    print(f"The approximate value of pi: {pi_value}")


main()
