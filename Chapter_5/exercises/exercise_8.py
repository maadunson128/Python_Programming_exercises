#program: caesian cipher

def main()->None:

    #getting input from the user
    message:str = input("Enter the message: ").lower()
    key:int = int(input('Enter the key value: '))
    

    string:str = 'a!b@c#d$e%f^g&h*i(j)k-l_m+n=o{p}[q]r|s\\t:u;v"w?x/y<z >'

    #Encoder
    encoded_str:str = ''


    #Algo for encoding in circular manner
    for ch in message:
        value:int = (string.find(ch) + 1+  key) % len(string)
        new_index:int
        print(value)
        if value == 0:
            new_index = len(string) - 1
        elif value in range(len(string)):
            new_index = value - 1
        print(new_index)
        encoded_str += string[new_index]

    print("The encoded message: {0}".format(encoded_str))

    #Decoder
    decoded_str:str = ''
    
    #decoding alogorithm in same circular manner
    for ch in encoded_str:
        value:int = (string.find(ch) + 1 - key) % len(string)
        new_index:int
        
        if value == 0:
            new_index = len(string) - 1
        elif value in range(len(string)):
            new_index = value - 1

        decoded_str += string[new_index]
        
    print("The decoded message: {0}".format(decoded_str))


main()
