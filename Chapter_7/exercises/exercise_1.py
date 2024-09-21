###Program: Payment for workers

def main()->None:

    #input for work hours, rate
    work_hrs = float(input("Enter the hours worked: "))
    rate_hr = float(input("Enter the wage (rate) for one hour: "))

    #wage calculation
    wage:float = 0
    if work_hrs > 40:
        wage = work_hrs * rate_hr * 1.5  #above 40 rate is 1.5 times the normal wage

    if work_hrs > 1 and work_hrs <=40:
        wage = work_hrs * rate_hr

    print(f"Total wage for {work_hrs} hours: {wage}")


main()
    
