###Program: Senator and citizenship Eligibility



'''A person is eligible to be a US senator if they are at least 30 years old
and have been a US citizen for at least 9 years. To be a US representative
these numbers are 25 and 7, respectively. Write a program that accepts a
person's age and years of citizenship as input and outputs their eligibility
for the Senate and House.'''

def main()->None:

    #user inputs:person's age, years of citizenship
    age:int = int(input("Enter you age: "))
    citizenship:int = int(input("Enter your years of citizenship: "))

    senator_age:int = 30
    senator_cit:int = 9
    represent_age:int = 25
    represent_cit:int = 7

    #Checking for eligiblity
    print("Eligibility for US senator: ")
    if age >= senator_age and citizenship >= senator_cit:
        print("You meet the eligibilty criteria and you are eligible.")
    else:
        print("You are not elogible as you don't meet the criteria.")

    print("Eligibilty for US representative: ")
    if age >= represent_age and citizenship >= represent_cit:
        print("You meet the eligibilty criteria and you are eligible.")
    else:
        print("You are not elogible as you don't meet the criteria.")


main()
    
