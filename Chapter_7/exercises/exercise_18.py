###Program: Exception handling

'''Take a favorite programming problem from a previous chapter and add
decisions and/ or exception handling as required to make it truly robust
(will not crash on any inputs). Trade your program with a friend and have
a contest to see who can ''break" the other's program.'''

#I have taken chaos problem for exception handling


def main()->None:

    try:
        #input from the user
        value_1:float = float(input("Enter the value 1: "))
        value_2:float = float(input("Enter the value 2: "))
        iteration:int = int(input("Enter the iterations: "))

        #Print top layer template with formatting
        print(f"{"index".ljust(9)}{str(value_1):<13}{str(value_2):<6}")
        print(28*'-')

        #calculating the values for each iteration
        x1:float = value_1
        x2:float = value_2
        for i in range(1, iteration + 1):
            x1 = 3.9 * x1 * (1 - x1)
            x2 = 3.9 * x2 * (1 - x2)

            #formatting the new values
            print(f"{i:^5}  {x1:0.6f}     {x2:0.6f}")

    except ValueError as err_name:
        if "could not convert string to float" in str(err_name):
            print("Please enter a valid float number.")
        elif "invalid literal for int() with base 10" in str(err_name):
            print("Please enter a valid integer number.")

    
        


main()



#ValueError: could not convert string to float: 'kd dd'
#ValueError: invalid literal for int() with base 10: '4.3'
