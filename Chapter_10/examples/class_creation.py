###Program: class creation

class example:
    def __init__(self, name):
        self.name = name

    def action1(self):
        print("Name:", self.name)

    def action2(self):
        print("Hello world!!!")
        

example1 = example('Pradeep')
example1.action1()
example1.action2()
