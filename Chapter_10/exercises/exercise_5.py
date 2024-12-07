###Program: Calculation of GPA

class Student:
    def __init__(self):
        '''This creates an instance of student with zero quality points and credits.
        This class will calculate the GPA of the student.
        '''
        self.quality_pts = 0
        self.credits = 0

    def addGrade(self, gradePoint, credit):
        '''This function will calculate the cumulative quality points and total credits fpr every subject.
        '''
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
        course_info = input("Enter the grade points and credits separated by comma: ")
        if not course_info:
            break
        
        points, credits = course_info.split(',')

        student1.addGrade(points, credits)

    print(f"Student 1 GPA: {student1.calculateGPA():.2f}")


main()