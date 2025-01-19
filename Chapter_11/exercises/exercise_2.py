#Program: Sort according to GPA, name, credits

class Student:
    '''Class for keep tracking of students info'''
    def __init__(self, name, hours, Qpoints):
        '''Initiates students details'''
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(Qpoints)

    def getName(self):
        '''Returns the name of the student'''
        return self.name
    
    def getHours(self):
        '''Returns the hours studied by the student'''
        return self.hours

    def getPoints(self):
        '''Returns the points earned by the student'''
        return self.qpoints
    
    def getGpa(self):
        '''Returns the GPA of the student'''
        return self.qpoints/self.hours
    
def getDetails():
    '''Used for getting input from user'''
    infile = input("Enter the file name to get details: ")
    sort_param = input("Enter the parameter on which sorting is to be done: ")
    outfile = input("Enter the filename for sorted students namelist to stored: ")

    return infile, sort_param, outfile


def makeStudent(details):
    '''Creates a Student class for details storing'''
    name, hours, points = details.split(",")
    return Student(name, hours, points)



def readStudents(infile_name):
    '''Reads the details from the file'''
    infile = open(infile_name, 'r')
    s = []
    for line in infile:
        s.append(makeStudent(line))

    infile.close()

    return s


def writeStudents(data, outfile_name):
    '''Writes the sorted details to file'''
    outfile = open(outfile_name, 'w')

    print(f"{"Name":12}{"Hours":10}{"Points":10}{"GPA":10}", file=outfile)
    for student in data:
        print(f"{student.getName():12}{student.getHours():10}{student.getPoints():10}{student.getGpa():10.3f}", file=outfile)

    outfile.close()

def main():

    #Prompt for asking the details from the user
    infile, sort_param, outfile = getDetails()

    #reading and sorting and storing the students based on details by user
    data = readStudents(infile)

    sort_values = {"name": Student.getName,
                    "hours": Student.getHours, 
                    "points": Student.getPoints,
                    "gpa": Student.getGpa}
    data.sort(key = sort_values[sort_param])

    writeStudents(data, outfile)

if __name__ == "__main__":
    main()