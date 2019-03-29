class Student:
    def __init__(self, fullName, age, height, complexion, residence, major):
        self.firstName = fullName.split()[0]
        self.lastName = fullName.split()[1:]
        self.age = age
        self.height = height
        self.complexion = complexion
        self.residence = residence
        self.major = major
    def changeFirstName(newName):
        self.firstName = newName
    def changeMajor(newMajor):
        self.major = newMajor
    def printNames(self):
        return self.firstName + " " + str(self.lastName)
    
def main():
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    height = eval(input("Enter your height: "))
    com = input("Enter your complexion: ")
    res = input("Enter your residence: ")
    major = "CS"
    ernest = Student(name, age, height, com, res, major)
    print(ernest.printNames())

main()
