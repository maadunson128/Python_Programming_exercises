###Program: Fuel efficiency of multi-leg journey (By using file)

#function to find for GPM
def find_gpm(file)->None:
    #initial ododmeter reading
    star_odo = float(file.readline())
    
    #asking for info for each leg journey
    info_readings = []
    while True:
        odometer:float = 0
        gas_consumed:float = 0

        #odomter and gas consumed readings from the textfile
        info = file.readline()
        if info == "":
            break

        #checking the values are separated by spaces
        try:
            odometer, gas_consumed = info.split()
        except ValueError:
            print(f"Please only enter the odometer and gas consumed readings separated by space correctly.")
            continue

        #adding the values into a list
        temp_list = [float(odometer), float(gas_consumed)]
        info_readings.append(temp_list)
        

    #finding the GPM for each leg and total travel
    total_gallons:float = 0.0
    current_miles:float = star_odo
    for i, element in enumerate(info_readings):
        total_gallons += element[1]
        print(f"MPG for leg {i+1}: {(element[0] - current_miles)/element[1]:.4f} miles per gallon")
        current_miles = element[0]

    print(f"Total MPG: {(current_miles - star_odo)/total_gallons:.4f} miles per gallon")
    
        
            
    
def main()->None:
    #Opening the text file in read mode
    filename = "exercise_10_ip.txt"
    file = open(filename, 'r')
    
    #finding the GPM for each leg and for total travel
    find_gpm(file)

main()
