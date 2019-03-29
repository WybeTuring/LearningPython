class AshesiStudent:
    def __init__(self, firstName, lastName, age, sex, yearGroup, major, residence, height, complexion, GPA):
        self.fname = firstName
        self.lname = lastName
        self.age = age
        self.sex = sex
        self.yearGroup = yearGroup
        self.major = major
        self.residence = residence
        self.height = height
        self.complexion = complexion
        self.GPA = GPA
'''
    def getLastName(self):return self.fname
    def getFirstName(self):return self.lname
    def getComplexion(self):return self.complexion
    def getHeight(self):return self.height
    def getAge(self):return self.age
    def getSex(self): return self.sex
    def getFullName(self): return self.fname + " " + self.lname
    def getGPA(self): return self.GPA
    def getMajor(self): return self.major
    def getResidence(self):return self.residence '''

karl = AshesiStudent("Karl", "Lemfon", 20, "M", 2022, "CS", "On Campus", 1.74, "red", 3.9)
print(karl.GPA)
karl.major = "MIS"
print(karl.major)
print(karl.fname + " " + karl.lname)
if karl.GPA >= 3.6 and karl.GPA <= 3.7:
    karl.Honours = "Cum Laude"
elif karl.GPA > 3.7 and karl.GPA <= 3.8:
    karl.Honours = "Magna Cum Laude"
elif karl.GPA > 3.8 and karl.GPA <= 4:
    karl.Honours = "Summa Cum Laude"

print(karl.Honours)


    
    
