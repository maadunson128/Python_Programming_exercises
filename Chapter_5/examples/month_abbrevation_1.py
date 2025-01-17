#month_abbrevation_1.py
#A program that abbrevates the name of a month, given it's number.

def main() ->None:

    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
             'September', 'October', 'November', 'December']
    month_no = int(input("Enter the number of the month: "))

    print("The abbrevation for the month number " + str(month_no) + ": " + month[month_no-1] + ".")

main()
