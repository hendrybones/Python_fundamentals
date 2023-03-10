class Person():

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name

    def getName(self):
        return self.name

        # To check if this person is employee

    def isEmployee(self):
        return False


# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())

# encapsulation

# polymorphims
class A():
    def show(self):
        print("Inside A")
class B():
    def show(self):
        print("Inside B")
# driver code
a = A()
A.show()
b= B()
b.show()




