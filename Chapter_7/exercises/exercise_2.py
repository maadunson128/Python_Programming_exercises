###Program: Grade for quiz

def main()->None:

    #input from the user for mark
    mark = int(input("Enter the marks (0-5): "))

    #grades:list[str] = ['F', 'F', 'D', 'C', 'B', 'A']

    #grade finding
    #grade:str = grades[mark]

    if mark == 0:
        grade = 'F'
    elif mark == 1:
        grade = 'F'
    elif mark == 2:
        grade ='D'
    elif mark == 3:
        grade = 'C'
    elif mark == 4:
        grade = 'B'
    elif mark == 5:
        grade = 'A'


        
    print(f"The grade for mark {mark} : {grade}")


main()
