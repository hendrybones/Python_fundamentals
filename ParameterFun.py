class Addition:
    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def calculate(self):
        print(self.first + self.second)


# Invoking parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

class Employee:
    def __int__(self):
        print('Employee created')
    def __del__(self):
        print('Destructor called, Employee deleted')
obj1= Employee()
del obj1

class Person():
    def __int__(self,name):
        self.name =name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employees(Person):
    def isEmployee(self):
        return True
emp = Person ("hendry")
print(emp.getName(),emp.isEmployee())
emp = Person("hendry2")
print(emp.getName(),emp.isEmployees())