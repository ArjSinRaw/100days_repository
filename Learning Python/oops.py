# a = 12
# b = 34
# print(" The sum of the two number is ", a+b)


# class RailwayForm:
#     formType = "railwayform"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")

# arjunApplication = RailwayForm()
# arjunApplication.name = 'Arjun'
# arjunApplication.train = 'Garib Rath'
# arjunApplication.printData()


# class Employee:
#     companyName = " Google"
#     salary ='5500'

# Arjun = Employee()
# Arjun.salary ='5000'
# Veeransh = Employee
# Veeransh.salary ='1000'
# print(Employee.companyName)
# Employee.companyName = "Meta"
# print(Veeransh.companyName) # it takes the udpated value
# print(Arjun.companyName) # it takes the udpated value 
# print(Arjun.salary)
# print(Veeransh.salary)
# print(Veeransh.age) # it shall throw the error as the set attribute if not there



class Employee:
    company = 'Google'
    def getSalary(self,greet):
        print(f"salary is {self.salary}")

@staticmethod
def greet():
    print(" Hello, Wie geht's")

Arjun = Employee()
Arjun.salary = 10000
Arjun.getSalary()
Arjun.greet()


