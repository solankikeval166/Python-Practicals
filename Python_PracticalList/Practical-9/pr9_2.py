fstd = open("student.txt", "a")
fmarks = open("marks.txt", "a")
ftotal = open("total.txt", "a")


name = input("Enter the name of the student :")
print("Name of the student is '{}':".format(name), file=fstd)

marks1 = eval(input("Enter the marks of 1st subject : "))
print("{}'s Marks of 1st subject is : ".format(name), marks1, file=fmarks)

marks2 = eval(input("Enter the marks of 2nd subject : "))
print("{}'s Marks of 2nd subject is : ".format(name), marks2, file=fmarks)

print(
    "{}'s total marks of both subject is : ".format(name), marks1 + marks2, file=ftotal
)

print("Operation Perfomed Successfully")
fstd.close()
fmarks.close()
ftotal.close()
