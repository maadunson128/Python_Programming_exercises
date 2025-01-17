###Program: Decoder using lists

def main()->None:
    encoded = input("Enter the Unicode encoded code: ")

    message = []
    for ch in encoded.split():
        message.append(chr(int(ch)))


    print("The decoded message: ", "".join(message))

main()
