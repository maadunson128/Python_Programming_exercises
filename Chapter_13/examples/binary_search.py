###Program: Binary search


arr = [1, 10, 3, 4, 56, 99, 34, 100, 104, 94, 10001, 4560]

arr.sort()


#Binary search function

def binarySearch(element, elm_list):
    n = len(elm_list)
    low = 0 
    high = n-1 

    while low<=high:
        mid = (low + high) //2

        if element == elm_list[mid]:
            return mid
        elif element < elm_list[mid]:
            high = mid - 1
        elif element > elm_list[mid]:
            low = mid + 1
    return -1

print(binarySearch(1012, arr))

