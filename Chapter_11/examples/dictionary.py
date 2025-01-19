def getFreq(pair):
    return pair[1]


def main()->None:

    fname = input("Enter the filename to analyse: ")
    infile = open(fname, 'r')

    text = infile.read()
    text.lower()

    for ch in '!"#$%&0*+,-./:;<=>?<0[\\]-_'{1}-':
        text = text.replace(ch, ' ')

    words = text.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    n = input("Enter the n top word count: ")

    items = list(counts.items())
    items.sort()
    items.sort(key=getFreq, reverse=True)

    for i in n:
        word, count = items[i]
        print(f"{word} \t {count}")


main()