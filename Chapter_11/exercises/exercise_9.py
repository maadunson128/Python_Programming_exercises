###program: list of records

#class for student
class Student:
    def __init__(self, name, hrs, pts):
        self.name = name
        self.hours = float(hrs)
        self.qpoints = float(pts)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQpoints(self):
        return self.qpoints

    def getGpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    name, hrs, pts = infoStr.split(',')
    return Student(name, hrs, pts)




def readStudents(filename:str)->None:
    infile = open(filename, 'r')
    s = []
    for line in infile:
        s_object = makeStudent(line)
        gpa = s_object.getGpa()
        s.append((gpa, s_object))
    infile.close()

    return s


def writeStudents(data, filename):
    outfile = open(filename, 'w')
    print("Name \t  Hours \t Points \t GPA", file=outfile)
    for gpa, line in data:
        print(f"{line.getName()} \t{line.getHours()} \t{line.getQpoints()}\t{gpa}", file=outfile)
    
    outfile.close()




def main()->None:

    filename = input("Enter the filename to read: ")
    data = readStudents(filename)
    data.sort()
    filename = input("Enter the file name to write: ")
    writeStudents(data, filename)
    print("The data has been written to the file.")

    

if __name__ == "__main__":
    main()