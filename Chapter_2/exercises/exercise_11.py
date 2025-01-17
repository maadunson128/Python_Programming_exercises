#Program: Unit conversion from tonnes to kilogram and gram

def intro():
    print("This program will do the following: ")
    print("1. It will get the input weight in tonnes from the user.")
    print("2. It will convert the tonnes into Kilogram and gram")

def conversion():
    tonne = eval(input("Enter the weight in tonnes: "))
    kilogram = tonne * 1000
    gram = kilogram * 1000
    print("Weight in Kilograms: ", kilogram, 'kilograms')
    print("Weight in grams: ", gram, 'grams')

intro()
conversion()