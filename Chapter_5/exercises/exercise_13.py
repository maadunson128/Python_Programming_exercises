#program: Using text files for input and output

def main()->None:

    #input from the files
    infile = open('exercise_13.txt', 'r')
    outfile = open('ex_13_output.txt', 'w')

    #reading the input va;lues from the text
    input_values = []
    for line in infile:
        input_values.append(line.strip())

    principal:float
    years:int
    interest:float

    principal = float(input_values[0])
    interest = float(input_values[1])
    years = int(input_values[2])

    #Heading text
    print(f"{"Year".ljust(9)}{"Value".ljust(7)}", file = outfile)
    print(16*'-', file = outfile)
    print(f"{0:^5}   ${float(principal):0.2f}", file = outfile)

    #calculating the future value
    for year in range(1, years+1):
        principal = principal + (principal) * (interest/100)
        
        output = f"{year:^5}   ${principal:0.2f}"
        print(output, file =outfile)

    #closing the files opened
    infile.close()
    outfile.close()

        
main()
        
