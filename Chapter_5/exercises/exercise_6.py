#Program: Value for input name(multi name)

def main()->None:
    #Getting the input from the user
    name:str = input("Enter the your name: ")
    name_list:list[str] = name.split()
    
    #Finding the value for the input name
    letters:list[str] = []

    for i in range(97, 123):
        letters.append(chr(i))

    value:int = 0
    for word in name_list:
        for letter in word:
            value = (letters.index(letter) + 1) + value


    print("The numeric value for your name {0}: {1}".format(name, value))

main()
