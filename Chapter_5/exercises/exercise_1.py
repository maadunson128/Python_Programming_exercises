#Program: Date conversion using string formatting


def main()->None:

    #getting the input date from the user
    date = input("Enter the date in the format (dd/mm/yyyy): ")

    #Formatting the given date in required format
    day:str
    month:str
    year:str
    day, month, year = date.split('/')

    months:list[String] = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

    month:String = months[int(month)-1][:3]

    print("The converted date: {0} {1:0>2}, {2}".format(month, day, year))

main()
    
    
