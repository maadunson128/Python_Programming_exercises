#Program: Average word length entered by user

def main()->None:

    #input from the user
    input_corpus:list[str] = input("Enter the corpus: ").split()

    #calculating the average word length
    count:int = 0
    for word in input_corpus:
        count += len(word)

    print(f"words: {count}\n Total: {len(input_corpus)}")
        
    avg_length:float = count / len(input_corpus)

    print(f"The average word length of corpus : {avg_length:0.0f}")

main()
