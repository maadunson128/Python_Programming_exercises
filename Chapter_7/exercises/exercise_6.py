###Program:


'''The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph
over the limit plus a penalty of $200 for any speed over 90 mph. Write a
program that accepts a speed limit and a clocked speed and either prints
a message indicating the speed was legal or prints the amount of the fine,
if the speed is illegal.'''


def speed_check(speed_limit:int, speed:float):

    print("--------------------------------------")
    print(f"Speed limit: {speed_limit}mph")
    print(f"Vehicle speed observed: {speed}mph")
    if speed > speed_limit or speed > 90:
        fine = penalty = 0
        print("Your speed was illegal.")
        if speed > speed_limit:
            fine = 50 + ((speed - speed_limit)* 5)
            print(f"Fine for crossing speed limit: ${fine}")
        if speed > 90:
            penalty = 200
            print(f"Penalty for crossing 90mph speed: ${penalty}")

        print(f"Total fine: ${fine + penalty}")
    else:
        print("You speed was legal.\nDrive safe within the speed limits")
    print("--------------------------------------")

    
def main()->None:
    #input from the user
    speed_limit:int = int(input("Enter the speed limit(mph): "))
    speed:float = float(input("Enter the speed of rider: "))

    #Speed checking and fine printing
    speed_check(speed_limit, speed)


main()

    
