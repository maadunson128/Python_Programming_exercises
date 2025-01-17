#Program: Encoder and decoder for caesian ciphers

def main()->None:
    '''
    This function encodes and decodes the message of the user input'''

    #Getting input
    text:str = input("Enter the text: ")
    key:int = int(input("Enter the keyt value: "))

    #Encoding the text

    encoded_msg:str = ''
    for letter in text:
        encoded_msg += (chr(ord(letter) + key))

    print("The encoded text: {0}".format(encoded_msg))

    #Decoding the encodinf message

    decoded_msg:str = ''
    for letter in encoded_msg:
        decoded_msg += (chr(ord(letter) - key))

    print("The decoded text: {0}".format(decoded_msg))
        


main()
