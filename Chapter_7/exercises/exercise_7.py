###Program: Babysitting bill

'''A babysitter charges $2.50 an hour until 9:00 PM when the rate drops to
$1.75 an hour (the children are in bed). Write a program that accepts a
starting time and ending time in hours and minutes and calculates the total
babysitting bill. You may assume that the starting and ending times are in
a single 24-hour period. Partial hours should be appropriately prorated.'''

def calculate_bill(s_hr:int, s_min:int, e_hr:int, e_min:int):
    tot_hr:int = 0
    tot_mins:int = 0
    rate_hr_1:float = 2.5
    rate_hr_2:float = 1.75
    amount_1:float = 0.0
    amount_2:float = 0.0
    
    #Total time babysitted calculation
    tot_hrs = e_hr - s_hr
    tot_mins = e_min - s_min
    if tot_mins < 0:
        tot_hrs -= 1
        tot_mins += 60

    print(f"Total time worked: {tot_hrs} hours {tot_mins} minutes")

    ###Calculation of rate for both slots
    
    #Total time babysitted till 9PM calculation
    tot_hrs_1:int = 0
    tot_mins_1:int = 0

    #converting starting and ending time into decimal
    s_time = s_hr + (s_min / 60)
    e_time = e_hr + (e_min / 60)

    value_1:float = 0.0
    value_2:float = 0.0
    time:float = 0.0

    '''
    Here, we are finding two values -> Value 1, value 2
    Value 1 -> How much hours fall before 9PM from starting time
    Value 2 -> How much hours fall before 9PM from ending time

    Then we are subracting the value 1 and value 2 to find how much hours below 9PM
    '''
    #finding the value 1 and value 2
    value_1 = 21.0 - s_time
    if (21.0 - e_time) > 0:
        value_2 = 21.0 - e_time
        
    #Decimal value that represents the duration(how much hours) fall before 9PM
    time = value_1 - value_2

    #Calculating the hours and minutes
    tot_hrs_1 = int(time)
    if time-tot_hrs_1 > 0:
        tot_mins_1 = round((time - tot_hrs_1) * 60, 2) #rounding off to handle the float precision mistakes.

    #calculation of amount for babysitting
    amount_1 = (tot_hrs_1 * rate_hr_1) + (rate_hr_1 / 60 * tot_mins_1)

    

 
    
    #Calculation of after 9PM working hours
    tot_hrs_2:float = 0
    tot_mins_2:float = 0
    
    tot_hrs_2 = tot_hrs - tot_hrs_1
    tot_mins_2 = tot_mins - tot_mins_1
    
    if tot_mins_2 < 0:
        tot_hrs_2 -=1
        tot_mins_2 += 60

    #Calculation of amount for slot 2 (time after 9PM)
    amount_2 = (tot_hrs_2 * rate_hr_2) + (rate_hr_2 / 60 * tot_mins_2)


    #Displaying the bill
    print(24*"-")
    print(f"Total time babysitted till 9PM: {tot_hrs_1}hrs {tot_mins_1:.0f}mins")
    print(f"Total time babysitted after 9PM: {tot_hrs_2}hrs {tot_mins_2:.0f}mins")
    print(f"Amount for babysitted till 9PM: ${amount_1}")
    print(f"Amount for babysitted after 9PM: ${amount_2}")
    print(24*"-")
    print(f"Total amount for babysitting: ${amount_1+amount_2}")
   
    


def main()->None:

    #input from the user
    #Inputs : starting hour, starting min, ending hour, ending min
    print(f"Please enter the timings in 24 hour format.")
    start_hr:int = int(input("Enter the starting hour: "))
    start_min:int = int(input("Enter the starting minute: "))
    end_hr:int = int(input("Enter the ending hour: "))
    end_min:int = int(input("Enter the ending minute: "))

    #calculating the bill
    calculate_bill(start_hr, start_min, end_hr, end_min)

main()
