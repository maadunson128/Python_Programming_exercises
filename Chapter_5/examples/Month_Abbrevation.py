#month_abbrevation.py
#A program that will print the abbrevation of the month, give its number.

def main() -> None:

    month_no = int(input("Enter the month number: "))

    month = 'JanFebMarAprMayJunJulAugSepOctNovDec'

    pos = (month_no - 1) * 3

    month_abb = month[pos : pos+3]

    print("The abbrevation of month number you entered: " + month_abb + ".")

main()
