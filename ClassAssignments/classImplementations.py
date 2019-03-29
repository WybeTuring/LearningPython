class AshesiStudent:
    def __init__(self, fullName, age, sex, yearGroup, major, residence):
        self.name = fullName
        self.age = age
        self.sex = sex
        self.yearGroup = yearGroup
        self.major = major
        self.residence = residence
        
    # The methods for changing the class attributes   
    def changeName(self, newName):
        self.name = newName
        
    def changeAge(self, newAge):
        self.age = newAge

    def changeSex(self, newSex):
        self.sex = newSex

    def changeYearGroup(self, newYearGroup):
        self.yearGroup = newYearGroup

    def changeMajor(self, newMajor):
        self.newMajor = newMajor

    def changeResidence(self, newResidence):
        self.residence = newResidence

    # The methods for getting information from the attributes
    def getNames(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getFirstName(self):
        return self.name.split()[0]

    def getSecondName(self):
        return self.name.split()[0]

    def getSex(self):
        return self.sex

    def getYearGroup(self):
        return self.yearGroup

    def getMajor(self):
        return self.major

    def getResidence(self):
        return self.residence

def main():
    # Creating a database of Ashesi students, the primary key will be a "autoNumber", that is assigned by how early on the student is registered
    # Instantiating the AshesiStudent class
    i = True
    k = 1
    students = []
    while i:
        fullName = input("Please enter your full names: ")
        age = int(input("Please enter your age: "))
        sex = input("What is your sex? [M/F/O]: ").upper()
        yearGroup = int(input("Please enter your year group: "))
        major = input("Please input your major [CS/ BA/ MIS/ CE/ ME/ EEE]: ").upper()
        residence = input("Are you on or off campus? ").lower().capitalize()
        var = "student" + str(k)
        var = AshesiStudent(fullName, age, sex, yearGroup, major, residence)
        students.append(var)
        k += 1
        i = int(input("Enter 1 to continue and 0 to stop: "))
    # Printing all the information of the registered students
    print("{0:5}".format(" "), end = "  ")
    print("{0:>30}".format("Full Names"), "{0:>5}".format("Age"), "{0:>3}".format("Sex"), "{0:>10}".format("Year Group"), "{0:^5}".format("Major"), "{0:>10}".format("Residence"),
          sep = "  ")
    j = 1
    for i in students:
        print("{0:5}".format(str(j)), end = "  ")
        print("{0:>30}".format(i.getNames()), "{0:>5}".format(i.getAge()), "{0:>3}".format(i.getSex()), "{0:>10}".format(i.getYearGroup()), "{0:>5}".format(i.getMajor()),
              "{0:>10}".format(i.getResidence()), sep = "  ")
        j += 1
    print("\n\nTHANK YOU!")
        

main()

    
