###Program: Attendee Manager

class Attendee:
    def __init__(self, name, company, state, email):
        'Creates an Attendee object to keep track of their data'
        self.name = name
        self.company = company
        self.state = state
        self.email = email


    def getName(self):
        'Returns name'
        return self.name
    
    def getCompany(self):
        '''Returns companny name'''
        return self.company
    
    def getState(self):
        'Returns State name'
        return self.state
    
    def getEmail(self):
        'Returns email'
        return self.email
    
    def getInfo(self):
        'displays the entire info'
        return self.name, self.company, self.state, self.email


class AttendeeManager:
    def __init__(self):
        'Reads data from the file'
        self.attendees = []
        infile = open('attendee.txt', 'r')

        for line in infile:
            name, company, state, email =  line.split(",")
            self.attendees.append(Attendee(name, company, state, email))
        infile.close()

    def getAttendee(self, name):
        'Returns the Attendee objects'
        for attendee in self.attendees:
            if attendee.getName() == "name":
                return attendee
            
    def addNewAttendee(self, name, company, state, email):
        'Makes new Attendee in the objects list'
        self.attendees.append(Attendee(name, company, state, email))

    def findByState(self, state):
        'Finds Attendee by state name'
        names = []
        for attendee in self.attendees:
            if attendee.getState().lower() == state.lower():
                names.append(attendee.getName())
        return names
            
    def delAttendee(self, name):
        'Deletes the attendee record by name'
        for i in range(0, len(self.attendees)):
            if self.attendees[i].getName() == name:
                del self.attendees[i]

    def updateFile(self):
        'Update the file with existing data'
        outfile = open('attendee.txt', 'w')
        for attendee in self.attendees:
            name, company, state, email = attendee.getInfo()
            print(name,company,state,email, sep=",",end="", file=outfile)

        outfile.close()



def main():
    manager = AttendeeManager()

    names = manager.findByState('TamilNadu')
    print(names)

main()