###Program: Built-in functions for list

def count(MyList, x):
    '''Count the occurences of x in list'''
    count = 0
    for element in MyList:
        if element == x: count += 1 

    return count


def isin(Mylist, x):
    '''Checks whether element x is in MyList'''
    ans = False
    for element in Mylist:
        if element == x: ans = True

    return ans

def index(Mylist, x):
    '''Returns the index of first occurence of the element x in MyList'''
    for i in range(len(Mylist)):
        if Mylist[i] == x:
            index = i
            break

    return index


def reverse(MyList):
    rev_list = []
    '''Reverses the list'''
    for element in MyList:
        rev_list = [element] + rev_list

    return rev_list

def sort(MyList):
    '''Sorts the list ascendingly'''
    sorted_list = []
    for i in range(len(MyList)):
        min_value = min(MyList)
        sorted_list.append(min_value)
        MyList.remove(min_value)

    return sorted_list

print(sort(['a', 'd', 'e', 'z', 'x']))

