#Program: Average of three exam scores

def average():
    score1, score2, score3 = eval(input("Enter the three scores separated by commas: "))
    average = (score1 + score2 + score3) / 3
    print("The average of three subjects: ", average)

average()