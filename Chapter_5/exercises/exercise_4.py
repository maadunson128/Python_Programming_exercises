#Program: Acronym for the input phrase

def main()->None:
    #getting input from the user
    phrase:str = input("Enter the phrase: ")

    #finding the acronym
    words:list[str] = list(phrase.split())

    acronym:str = ""
    for word in words:
        acronym = acronym + word[0].upper()

    print("The acronym for the input phrase: {}".format(acronym))

main()
        
    
