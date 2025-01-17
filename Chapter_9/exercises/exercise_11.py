###Program: Simulating estimate the probability of 
###rolling five of a kind in a single roll of five six-sided dice.

from random import randint

#function for information
def info()->None:
    print("This is a simulation that will simulate the rolling of five six-sided dice in single roll.")

#simulating the event n times
def simNtimes(n:int)->float:
    event_happen:int = 0
    for _ in range(n):
        dice1:int = randint(1,6)
        dice2:int = randint(1,6)
        dice3:int = randint(1,6)
        dice4:int = randint(1,6)
        dice5:int = randint(1,6)

        if dice1 == dice2 == dice3 == dice4 == dice5:
            event_happen += 1

    return event_happen / n

def main()->None:
    #info about the simulation
    info()

    #getting the input: number of trials
    n:int = int(input("Enter the number of trials: "))

    #simulating the dices thrown
    probability:float = simNtimes(n)

    #final result
    print("Event: rolling five of a kind in a single roll of five six-sided dice")
    print(f"The probality of the given above event: {probability}")


main()
