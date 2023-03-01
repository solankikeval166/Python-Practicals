# D) Find who will be first among two students using polymorphism.

class Student:
    def _init_(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks, end="\n\n")

    def _gt_(self, other):
        if self.marks > other.marks:
            return True
        else:
            return False


student1 = Student("Bhargav", 19, 89.46)
student2 = Student("Karan", 20, 78.24)
print("\nStudent 1:")
student1.display()
print("Student 2:")
student2.display()

print("----------------")
if student1 > student2:
    print(student1.name, "is first")
else:
    print(student2.name, "is first")
print("----------------")
