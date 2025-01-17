###Program: To convert the string list into  int list

def intList(strList)->None:

    for i, element in enumerate(strList):
        strList[i] = int(strList[i])


def main()->None:

    #Getting the string List from the user as input
    strList:list[str] = list(eval(input("Enter the string elements for the list: ")))

    #printing the details of the list and its elements before modification
    type_element_before = [type(element) for element in strList]
    print(f"Before Modifying:\n List: {strList} \t Type: {type(strList)} \nElement types in the list: {type_element_before}\n")

    #Modifying the entire string list as integer list
    intList(strList)

    #printing the details of the list and its elements after modification
    type_element_after = [type(element) for element in strList]
    print(f"After Modifying:\n List: {strList} \t Type: {type(strList)} \nElement types in the list: {type_element_after}")


main()
