#declaring class Employee
class Employee:
    
#initializes constructor 
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

#display function for display information
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary, end="\n\n")

#updatedSalary function will calculate increased salary 
    def updatedSalary(self):
        self.salary = self.salary * 1.04
        print("Updated Salary ", self.salary)

#creating a emp object 
emp = Employee("Keval", 18, 1000)

emp.display()