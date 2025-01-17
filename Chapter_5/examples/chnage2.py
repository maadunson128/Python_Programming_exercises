#Program: A better program for claculate the total value

def main()->None:

    #Getting the inputs from the user for the count of different coins
    paise_25 = int(input("Enter the total number of 25 paise: "))
    paise_10 = int(input("Enter the total number of 10 paise: "))
    paise_5 = int(input("Enter the total number of 5 paise: "))
    paise_2 = int(input("Enter the total number of 2 paise: "))

    #Calculating the value for coins
    total = 25*paise_25 + 10*paise_10 + 5*paise_5 + paise_2

    print("Toal value for your coins: {0}.{1:0>2}Rs.".format(total//100, total%100))


main()
