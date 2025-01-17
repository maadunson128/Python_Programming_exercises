###Program: Finding the best student

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


    
def main()->None:

    file = input("Enter the students file name: ")

    #opening the file in read mode
    infile = open(file, 'r')

    #first student as best student
    best = makeStudent(infile.readline())

    list_best = [best]
    for line in infile:
        s = makeStudent(line)

        if s.getGpa() >= best.getGpa():
            list_best.append(s)


    infile.close()

    print("The best students details:")
    print("Name \t \t Hours \t\t Points\t\tGpa")
    for best in list_best:
        print(best.getName(), best.getHours(), best.getQpoints(), best.getGpa(), sep='\t\t')


main()
    









            
