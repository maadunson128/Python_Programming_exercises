###Program: Table for windchill index

def create_table()->None:

    #creating the values of index table
    wind_index = []
    for T in range(-20, 61, 10):
        temp = []
        for V in range(0, 51, 5):
            if V < 3: #handling the case where the speed is less than 3mph
                temp.append("NA")
            else:
                temp.append(round((35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)), 3)) #formula for windchill value
        wind_index.append(temp)

    #printing the header row
    print(f"{"Temp/Speed":^10}", sep="", end="")
    for i in range(0, 51, 5):
        print(f"{i:^10}", sep="", end="")
    print(f"\n{125*"_"}\n")

    #printing the rows with the values for each T value
    i = -20
    for elem_1 in wind_index:
        str_temp = ""
        for elem_2 in elem_1:
            str_temp += f"{elem_2:^10}"
        print(f"{i:^10}{str_temp}\n\n")
        i += 10
    
def main()->None:

    #creating table for windchill index
    create_table()


main()
