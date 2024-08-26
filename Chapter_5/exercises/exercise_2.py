#Program: Grade for corresponding scale

def main()->None:
    #getting the user input->score
    score = int(input("Enter the score (0-5): "))

    #finding the corresponding grade for the score
    grades:list[str] = ['F', 'F', 'D', 'C', 'B', 'A']

    grade:str = grades[score]

    print("The grade for the score {0}: {1}".format(score, grade))

main()

    
