from person import Person

class Teacher(Person):

    def __init__(self, firstName, lastName, middleName, id, type, department, position):
        super().__init__(firstName, lastName, middleName, id, type)
        self.department = department
        self.position = position


    def getDepPos(self):
        return (f'{self.department} {self.position}')



class Load(Teacher):

    def __init__(self, subject):
        self.subject = subject

    def getSub(self):
        return self.subject

