#Program: Functionality like 'wc' in Unix/Linux

def main()->None:
    #getting the file name as input
    file_name:str = input("Enter the file name with extension: ")

    #opening the file
    infile = open(file_name, 'r')

    #counting the lines
    lines:list[str] = infile.readlines()
    lines_count:int = len(lines)
    

    #counting the words, characters
    words_count:int = 0
    characters_count:int = 0
    
    for line in lines:
        #counting the word count
        words_count += len(line.split())
        
        for word in line:
            #counting the characters count
            characters_count += len(word)

    print(f"Line count: {lines_count}\nWords count: {words_count}\nCharacters count:{characters_count}")
        

main()
