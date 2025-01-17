###Program: HDD and CDD
##HDD: Heating Degree Days
##CDD: Cooling Degree Days

#function for calculating HDD and CDD
def calculate_total(avg_temp:list[float])->float:
    hdd:float = 0.0
    cdd:float = 0.0

    #calculating running total of hdd and cdd
    for temp in avg_temp:
        if temp < 60:
            hdd += (60-temp)
        elif temp > 80:
            cdd += (temp - 80)

    print(f"HDD: {hdd} degree days.\nCDD: {cdd} degree days.")
             
    return hdd + cdd
    

def main()->None:

    #user input: sequence of average temperatures
    avg_temperatures:list[str] = input("Enter the average temperatures separated by space: ").split()
    avg_temperatures:list[float] = [float(x) for x in avg_temperatures]

    #calculating HDD and CDD total days
    total:float = calculate_total(avg_temperatures)

    print(f"Total of HDD and CDD: {total} degree days.")

main()
