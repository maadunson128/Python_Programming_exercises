###Program: 4-Word Replacer


def checkEligibilty(word):
    cnd1, cnd2 = True, True
    if len(word) != 4:
        cnd1 = False
    for i in word:
        if i in [',', '.', ':', ';', '?', '[', ']', '{' '}']:
            cnd2 = False

    return cnd1 and cnd2


def main()->None:

    #opening the file
    infile = open("input_11.txt", "r")
    outfile = open("output_11.txt", 'w')


    for line in infile:
        words = line.split()

        for word in words:
            if checkEligibilty(word):
                print("*" *len(word), file = outfile, end=" ")
            else:
                print(word, file=outfile, end=' ')

        print(file=outfile)


if __name__ == "__main__":
    main()
