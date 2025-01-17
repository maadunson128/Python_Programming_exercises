###Program: Sum of square of numbers


#function for converting the list into int list
def intList(strList)->None:
    for i, element in enumerate(strList):
        strList[i] = int(strList[i].strip())
    print(strList)
    return strList


#function to find sum of elements in a list
def sumList(list_num:list[int])->int:
    #using sum() function to return sum of the sequence
    return sum(list_num)


#function to square a number
def square(num:float)->int:
    return num **2

#function to square each element in a list
def squareEach(nums)->None:
    #squaring each element in the list
    for i, num in enumerate(nums):
        nums[i] = square(num)

    


def main()->None:

    #opening a file to read
    file_read = open('exer_14_data.txt', 'r')
    file_write = open('exer_14_data.txt', 'a')

    str_list:list[str] = file_read.readlines()
    #taking each number from the file for numbers

    #converting the string list into int list
    int_list = intList(str_list)

    
    #squaring the each terms in the list
    squareEach(int_list)

    #sum of elemnts in the list
    sum_list = sumList(int_list)

    #Printing the sum of squares of elements from the file
    print(f"Sum of squares of elements in the list: {sum_list}")

    #closing the read file
    file_read.close()
    
    file_write.write(f"\nsum of squares of above numbers: {sum_list}")

    #closing the append file object
    file_write.close()
    
    

main()

    
    
    
    
