###program: Field of vision

import random
import math
#function for intro
def intro()->None:
    print("This program will simulate the field of vision when you are halfway between the center of cube and the wall at front.")
    print("The walls are at x = +-1, y = +-1, z = +-1 representing 6 walls (front, back, left, right, top bottom)")
    print("Our latest position is at x, y, z = (0.5, 0, 0)")
    
#function for generating random distances 
def generate_distance_pts()->tuple[float, float, float]:
    x:float = 0
    y:float = 0
    z:float = 0

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    z = random.uniform(-1, 1)

    return x, y, z

#function for normalising the distance points to get direction vectors
def normalise(x:float, y:float, z:float)->tuple[float, float, float]:
    length:float = math.sqrt(x**2 + y**2 + z**2)

    return x/length, y/length, z/length

#function for checking if the direction vectors intersect the larger wall.
def check_intersect(dx:float, dy:float, dz:float)->bool:
    # we are located at 0.5, 0, 0
    if dx > 0:
        t:float = 0.5 / dx #distance that extends the point to the wall
        dy_intersect:float = t * dy
        dz_intersect:float = t*dz

        if abs(dy_intersect) <= 1 and abs(dz_intersect) <= 1:
            return True

    return False

#simulating each direction 
def simEach()->bool:
    x:int = 0
    y:int = 0
    z:int = 0
    #random direction generation
    x, y, z = generate_distance_pts()  # it genrates the distance points within the wall bounds

    #normalising the x,y,z points to get random direction from random distance points
    dx, dy, dz = normalise(x, y, z)

    #checking whether it intersects the larger wall
    result:bool = check_intersect(dx, dy, dz)

    return result

    
def simView(n:int)->int:
    hits_wall:int = 0 #no times the larger wall has been seen
    for _ in range(n):
        hits:bool = simEach()

        if hits:
            hits_wall += 1

    return hits_wall
#function for result displaying the field of view
def result(hits, total)->None:
    print(f"The field of view of larger front wall is: {hits/total}")

    
def main()->None:

    #simulation intro
    intro()

    n:int = 987678  #no of times for simulation

    #monte carlo simulation
    hits_wall = simView(n)

    #result
    result(hits_wall, n)


main()
