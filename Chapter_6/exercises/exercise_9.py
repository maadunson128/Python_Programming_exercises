###Program: Grade of score

#function for grade calculation
def calculate_grade(score:int)->str:
    #matching the grade
    grade:str
    if score in range(90, 101):
        grade = 'A'
    elif score in range(80, 90):
        grade = 'B'
    elif score in range(70, 80):
        grade = 'C'
    elif score in range(60, 70):
        grade = 'D'
    elif score in range(0, 60):
        grade = 'F'

    return grade


def main()->None:

    #getting the user input score
    score:int = int(input("Enter the score (0-100): "))

    #grade finding
    grade:str = calculate_grade(score)

    print(f"The grade for the score {score} : {grade}")

main()
