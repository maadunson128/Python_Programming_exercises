from random import randint

#function for simulating initial roll
def initial_roll()->tuple[str, int]:
    result:str = ''
    point:int = 0

    out:int = randint(1, 6) + randint(1, 6) #simulating random two dice rolls

    if out in [2, 3, 12]:return 'L', point
    elif out in [7, 11]: return 'W', point
    elif out in [4, 5, 6, 8, 9, 10]: return 'C', out

for _ in range(1001):
    result = initial_roll()
    print(result)
