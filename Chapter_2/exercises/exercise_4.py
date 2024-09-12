#Program: Temperature conversion using for loop (counted loop)

def main():
    celsius = eval(input("Enter the temperature in degree celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print("Temperature in fahreheit: ", fahrenheit, "degree fahrenheit")

for i in range(5):
    main()