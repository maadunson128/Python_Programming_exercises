#Program: To draw a horizontal bar chart for students marks

#importing libraries
from graphics import *

def main()->None:

    #opening the file
    infile = open('ex_15_input.txt', 'r')

    #getting input from the file
    count:int = int(infile.readline())

    #storing the students names and marks
    student_name:list[str] = []
    marks:list[int] = []
    for i in range(count):
        details = infile.readline().split()
        student_name.append("".join(details[0:-1])) 
        marks.append(int(details[-1]))


    #Window creation according to students count
    win = GraphWin('Window', 600, (count * 25)+50)

    #Initial values for text and the rectangle(marks)
    x:int = 70
    y:int = 37
    x1:int = 300
    y1:int = 25
    y2:int = 40
    
    for i in range(len(student_name)):
        #drawing the names on left
        Text(Point(x + (float(len(student_name[i])/2) * 8.2), y), student_name[i]).draw(win)
        x2:int = x1 + (marks[i] * 2.5)
        #drawing the marks as shapes
        Rectangle(Point(x1, y1), Point(x2, y2)).draw(win)
        #updating the values
        y1 += 25
        y2 += 25
        y += 25


        
main()


