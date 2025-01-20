###Program: Word Replacer


def main()->None:

    #opening the files for operations
    infile = open("input_12.txt", "r")
    c_file = open("censored.txt", "r")
    outfile = open("output_12.txt", "w")

    #making censored words list
    for line in c_file:
        censored_list = line.split()
        
    #word censoring functionality
    for line in infile:
        words = line.split()

        for word in words:
            if word in censored_list:
                print("*" *len(word), file = outfile, end=" ")
            else:
                print(word, file=outfile, end=' ')

        print(file=outfile)


if __name__ == "__main__":
    main()
