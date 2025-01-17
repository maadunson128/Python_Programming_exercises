#Program: Data conversion

def main()->None:

    #getting the input string for data
    data:String = input("Enter a data (dd/mm/yyyy): ")
    
    #splitting the datas separately
    date_str, month_str, year_str = data.split('/')
    
    months:list[String] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']

    month:String = months[int(month_str) - 1]
    #Formatting the string into another format
    final_date:String = f"{month} {date_str}, {year_str}"
    print("The date after conversion:", final_date)

main()
