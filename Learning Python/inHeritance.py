class Employee:
    company = 'Google'

    def showDetails(self):
        print("This is an employee")

class proGrammer(Employee):
    language = 'python'
   
    def getLanguage(self):
        print(f"The language selected is {self.language}")

e = Employee()
e.showDetails()
p = proGrammer()
p.showDetails()
print(p.company)
        