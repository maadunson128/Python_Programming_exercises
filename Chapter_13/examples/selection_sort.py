arr = [1, 99, 83, 24, 56, 75, 45]

n = len(arr)
for i in range(n-1):
    min = i
    for j in range(i, n):
        if arr[min] > arr[j]:
            min = j

    arr[min], arr[i] = arr[i], arr[min]


print(arr)
