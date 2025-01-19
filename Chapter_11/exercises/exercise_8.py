###Program: Removing duplicates

def remove_dup(MyList):
    dict = {}
    for i in MyList:
        dict[i] = dict.get(i, 0) + 1

    for key in dict.keys():
        n = dict.get(key)
        for i in range(n-1):
            MyList.remove(key)

    print(MyList)


remove_dup(['cat', 'cat', 'dog', 'anime', 'anime'])