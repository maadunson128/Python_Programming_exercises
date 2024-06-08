#Program: Pause the program for the user to read

def main():
    print("This program will do the following steps:")
    print("1. It will get the temperature in degree celsius.")
    print("2. Then it will convert the celsius to Farenheit.")
    print("3. It will display the temperature in Fahrenheit")

    celsius = eval(input("Enter the temperature in degree celsius: "))
    fahreheit = 9/5 * celsius + 32
    print("Temperature in Fahrenheit : ", fahreheit, "degree fahreheit.")

main()


input("Enter <Enter> to quit.")