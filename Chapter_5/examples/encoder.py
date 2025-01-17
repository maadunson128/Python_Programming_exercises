###Program: Creating our own encoder

def main() -> None :
    #Getting the message from the user
    message = input("Enter a message: ")

    print("Here is the encoded unicodes: ")
    #Encoding the message in Unicode.
    for ch in message:
        print(ord(ch), end=' ')


main()
