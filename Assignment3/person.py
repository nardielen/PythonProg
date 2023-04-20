class Person:

    def __init__(self, firstName, lastName, middleName, id , type):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.id = id
        self.type = type


    def getName(self):
        return (f'{self.lastName}, {self.firstName} {self.middleName}.')

    def getID(self):
        return self.id

    def getType(self):
        return self.type