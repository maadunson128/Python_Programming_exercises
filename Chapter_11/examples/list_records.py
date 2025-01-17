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
        s.append(makeStudent(line))
    infile.close()

    return s


def writeStudents(data, filename):
    outfile = open(filename, 'w')
    for line in data:
        print(f"{line.getName()} \t{line.getHours()} \t{line.getQpoints()}", file=outfile)
    
    outfile.close()




def main()->None:

    filename = input("Enter the filename to read: ")
    data = readStudents(filename)
    data.sort(key=Student.getGpa)
    filename = input("Enter the file name to write: ")
    writeStudents(data, filename)
    print("The data has been written to the file.")

if __name__ == "__main__":
    main()