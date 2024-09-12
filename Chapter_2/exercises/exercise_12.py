#Program: Interactive Calculator

def calculator():
    calculation = eval(input("Enter the mathematical expression: "))
    print("The answer for the mathematical epression: ", calculation)

for i in range(100):
    calculator()