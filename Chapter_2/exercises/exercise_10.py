#Program: Coonversion from Kms to miles

def conversion():
    kilometer = eval(input("Enter the distance in Kilometers: "))
    miles = 0.62 * kilometer
    print("The distance travelled in miles: ", miles, ' miles')

conversion()