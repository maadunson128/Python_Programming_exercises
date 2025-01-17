###Program: BMI alert

'''The body mass index (BMI) is calculated as a person's weight (in pounds)
times 720, divided by the square of the person's height (in inches). A BMI
in the range 19-25, inclusive, is considered healthy. Write a program that
calculates a person's BMI and prints a message telling whether they are
above, within, or below the healthy range.'''

def find_BMI(weight:float, height:float)->float:
    #BMI calculation
    return (weight * 720) / height**2

def main()->None:

    #input from user for weight and height
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))

    #calculating BMI
    BMI = find_BMI(weight, height)
    #print(f"Your BMI : {BMI}")

    if BMI >= 19 and BMI <= 25:
        print("You are healthy and you are within the healthy limit.")
    elif BMI < 19:
        print("You are below the healthy BMI limit.")
    elif BMI > 25:
        print("You are above the healthy BMI limit.")

main()
    
    
