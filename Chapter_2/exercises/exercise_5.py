#Program: Display temperatures in celsius and fahrnheit as table

def main():
    print("Celsius", '\t\t', 'Fahrenheit')
    for celsius in range(0,101,10):
        fahrenheit = 9/5 * celsius + 32
        print(celsius,"C",'\t\t\t', fahrenheit,'F')

main()
