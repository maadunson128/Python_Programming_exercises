#Program: Conversion from FAhrenheit to celsius

def conversion():
    fahrenheit = eval(input("Enter the temperaturein fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature in degree celsius: ", celsius)

conversion()