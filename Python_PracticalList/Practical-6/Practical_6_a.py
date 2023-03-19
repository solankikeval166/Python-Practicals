# Consider an example of declaring the examination result. Design three classes:
# Student, Exam, and Result. The Student class has data members such as those
# representing rollNumber, Name, etc. Create the class Exam by inheriting Student
# class. The Exam class adds fields representing the marks scored in six subjects. Derive
# Result from the Exam class, and it has its own fields such as total marks. Write an
# interactive program to model this relationship.
class Student:
    def __init__(self, rollNumber, name):
        self.rollNumber = rollNumber
        self.name = name


class Exam(Student):
    def __init__(self, rollNumber, name, marks):
        super().__init__(rollNumber, name)
        self.marks = marks


class Result(Exam):
    def __init__(self, rollNumber, name, marks):
        super().__init__(rollNumber, name, marks)
        self.totalMarks = 0

        for mark in marks:
            self.totalMarks += (mark)

        self.grade = self.calculate_grade()

    def calculate_grade(self):
        percentage = self.totalMarks / 6
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"


# Main Section

rollNumber = input("Enter student's roll number: ")
name = input("Enter student's name: ")

marklist = []

for i in range(6):
    print("Enter mark of subject" ,i)
    mark = int(input())
    marklist.append(mark)

result = Result(rollNumber, name, marklist)

print("Total marks:", result.totalMarks)
print("Grade:", result.grade)
