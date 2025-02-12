###Program: Shuffle list
import random


def shuffle(MyList):
    n = len(MyList)
    index_list = [i for i in range(n)]
    shuffle_list = [0 for i in range(n)]
    for i in range(n):
        rv = random.choice(index_list)
        index_list.remove(rv)
        shuffle_list[rv] = MyList[i]

    return shuffle_list

def main():
    print(shuffle([1, 2, 3, 4, 5, 39]))

if __name__ == "__main__":
    main()