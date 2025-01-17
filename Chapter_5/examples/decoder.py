###Program: Decoder that decodes the Unicode encoded code

def main()->None:
    encoded:String = input("Enter the Unicode encoded code: ")

    #Here, the list message is used as accumulator instead of a string
    message = ""
    for ch in encoded.split():
        message = message + chr(int(ch))

    print("The decoded message:", message)


main()
    
