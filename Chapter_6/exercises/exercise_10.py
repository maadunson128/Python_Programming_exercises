###Program: To find acronym for the input phrase

def find_acronym(phrase)->str:
    
    #finding the acronym
    words:list[str] = list(phrase.split())

    acronym:str = ""
    for word in words:
        acronym = acronym + word[0].upper()
    return acronym

def main()->None:

    #user input for phrase
    phrase:str = input("Enter the phrase: ")

    acronym = find_acronym(phrase)

    print(f"The acronym for the phrase: {acronym}")


main()

    
