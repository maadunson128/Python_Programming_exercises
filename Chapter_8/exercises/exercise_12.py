###Program: HDD and CDD using file
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
    #opening a text file in read mode
    filename = "exercise_12_ip.txt"
    infile = open(filename, 'r')

    avg_temperatures:list[str] = infile.readline().split()
    avg_temperatures:list[float] = [float(x) for x in avg_temperatures]

    #calculating HDD and CDD total days
    total:float = calculate_total(avg_temperatures)

    print(f"Total of HDD and CDD: {total} degree days.")

    infile.close()

main()
