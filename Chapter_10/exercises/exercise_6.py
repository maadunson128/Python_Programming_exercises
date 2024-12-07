###Program: Calculation of GPA

class Student:
    def __init__(self):
        '''This creates an instance of student with zero quality points and credits.
        This class will calculate the GPA of the student.
        '''
        self.quality_pts = 0
        self.credits = 0

    def addGrade(self, letterGrade, credit):
        '''This function will calculate the cumulative quality points and total credits fpr every subject.
        '''
        grade_point_dict = {
            'O': 10,
            'A+': 9,
            'A': 8,
            'B+': 7,
            'B': 6,
            'C': 5
        }
        #converting the letetr grade into grade points
        gradePoint = grade_point_dict.get(letterGrade, 0)

        self.quality_pts += float(gradePoint) * int(credit)
        self.credits += int(credit)

    def calculateGPA(self):
        '''This function will calculate the GPA of the student.'''
        return self.quality_pts/self.credits
    

def main()->None:

    #creating student object
    student1 = Student()

    #asking the user to enter the course details
    while True:
        course_info = input("Enter the letter grade and credits separated by space : ")
        if not course_info:
            break
        
        letterGrade, credits = course_info.split()

        student1.addGrade(letterGrade.upper(), credits)

    print(f"Student 1 GPA: {student1.calculateGPA():.2f}")


main()