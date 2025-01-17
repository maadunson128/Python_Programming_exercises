###Program: Simulation of two dimensional walk in blocks of city
from random import randint

#info function
def info()->None:
    print("This is a simulation of walking in blocks of city.")
    print("Each step is forward, backward, left, right that is simulated based on randomness. + \
            \nIt will give the final position of the person.")

#simulation function
def simSteps(n:int)->tuple[int, str, int, str]:

    #assuming the person position is 0, 0
    initial_x:int = 0
    initial_y:int = 0
    vertical_steps:int = 0
    horizontal_steps:int = 0
    
    for _ in range(n):
        step:int = randint(1,4)
        #simulating the each step by random values
        if step == 1: vertical_steps +=1
        elif step == 2: vertical_steps -= 1
        elif step == 3: horizontal_steps += 1
        elif step == 4: horizontal_steps -= 1

    
    value1_direction:str = ''
    value2_direction:str = ''
    
    if vertical_steps - initial_y > 0:
        value1_direction = 'front'
    else: value1_direction = 'back'

    if horizontal_steps - initial_x > 0: value2_direction = 'left'
    else: value2_direction = 'right'

    return abs(vertical_steps - initial_y), value1_direction, abs(horizontal_steps - initial_x), value2_direction

        
def main()->None:

    #info about the simulation
    info()


    #input: no of steps
    n:int = int(input("Enter the number of steps to simulate: "))

    #simulating the steps
    first, f_b, second, l_r = simSteps(n)

    #final position
    print(f"You are {first} steps {f_b} and {second} steps {l_r}")

main()
