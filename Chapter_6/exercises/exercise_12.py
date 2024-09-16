###Program: Sum of elements in a list

def sumList(list_num:list[float])->float:

    #using sum() function to return sum of the sequence

    return sum(list_num)

def main()->None:

    #list for the sum
    list_num:list[float] = list(eval(input("Enter the list of numbers separated by comma: ")))

    #Calculating the sum of the elemnts inthe list
    print(f'Sum of elements in the list: {sumList(list_num)}')


main()
