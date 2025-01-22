###Program: Random walk in Sidewalk

from random import choice

def main()->None:

    n:int = int(input("Enter the  number of steps: "))

    dict ={}
    for i in range(1, n+1):
        dict[i] = 0



    current_position = n//2

    while True:
        if current_position <=1 or current_position >= n:
            break

        coin_res = choice(['H', 'T'])

        if coin_res == 'H':
            current_position += 1
        elif coin_res == 'T':
            current_position -= 1

        dict[current_position] = dict.get(current_position, 0) + 1

    
    for key, value in dict.items():
        print(f"Square {key} : {value} times ")


if __name__ == "__main__":
    main()


