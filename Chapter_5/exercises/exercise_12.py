#Program: Modified version of future value program

def main()->None:

    #input from the user
    principal:float = float(input("Enter the principal amount: "))
    interest:float = float(input("Enter the interest percentage: "))
    years:int = int(input("Enter the number of years: "))

    #Heading text
    print(f"{"Year".ljust(9)}{"Value".ljust(7)}")
    print(14*'-')
    print(f"{0:^5}   ${principal:0.2f}")

    #calculating the future value
    for year in range(1, years+1):
        principal = principal + (principal) * (interest/100)
        
        print(f"{year:^5}   ${principal:0.2f}")
    


main()
    
