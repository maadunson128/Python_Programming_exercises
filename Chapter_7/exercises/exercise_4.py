###Program: Class classification from credits


'''A certain college classifies students according to credits earned. A student
with less than 7 credits is a Freshman. At least 7 credits are required to be
a Sophomore, 16 to be a Junior and 26 to be classified as a Senior. Write a
program that calculates class standing from the number of credits earned.'''

def find_class(credits:int)->str:

    #I hope the full credits has to be secured in the respective year to go to next year. Also the credits is assumed to be integer.
    class1 = ''
    if credits >= 26:
        class1 = 'Senior'
    elif credits >= 16:
        class1 = 'Junior'
    elif credits >= 7:
        class1 = 'Sophomore'
    elif credits > 0 and credits < 7:
        class1 = 'Freshman'

    return class1


def main()->None:

    #input from the user for credits
    credits = int(input("Enter the credits: "))

    #finding the class
    class_s = find_class(credits)

    print(f"The class for credit {credits}: {class_s}")

main()
        
