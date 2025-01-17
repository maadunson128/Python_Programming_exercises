###Program: Grade for 100 marks exam

def find_grade(marks:float)->str:

    #grade finding
    grade = '' 
    if marks >= 90 and marks <= 100:
        grade = 'A'
    elif marks >= 80 and marks <=89:
        grade = 'B'
    elif marks >= 70 and marks <= 79:
        grade = 'C'
    elif marks >= 60 and marks <= 69:
        grade = 'D'
    elif marks < 60:
        grade = 'F'
        
    return grade
    
def main()->None:
    #user input for marks
    marks:float = float(input("Enter the marks (0-100): "))

    grade = ''
    #calculate grade
    grade:str = find_grade(marks)

    print(f"The grade for {marks} mark : {grade}")

main()
    

    
    
