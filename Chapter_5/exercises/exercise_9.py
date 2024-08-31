#Program: To count the number of words

def main()->None:

    #input from the user
    input_corpus:list[str] = input("Enter the corpus: ").split()

    print(f"The number of words in the corpus: {len(input_corpus)}")

main()
