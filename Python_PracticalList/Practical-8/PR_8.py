import sqlite3

conn = sqlite3.connect("test_abc.db")
print("\nopened database successfully\n")
c = conn.cursor()
# c.execute(
#     """CREATE TABLE student(
#     FIRST text,
#     LAST text,
#     AGE INT,
#     EMAIL text,
#     ID VARCHAR
# )"""
# )
print("Table created Successfully\n")
c.execute("select sqlite_version();")
data = c.fetchone()
print("Database version : %s \n" % data)
c.execute(
    "INSERT INTO student (FIRST,LAST,AGE,EMAIL,ID)\
VALUES('Keval','Solanki',18,'21ce137@charusat.edu.in',1)"
)
c.execute(
    "INSERT INTO student (FIRST,LAST,AGE,EMAIL,ID)\
VALUES('Poorv','Sinojiya',19,'21ce135@charusat.edu.in',2)"
)
c.execute(
    "INSERT INTO student (FIRST,LAST,AGE,EMAIL,ID)\
VALUES('Krishna','Shah',20,'21ce128@charusat.edu.in',3)"
)
c.execute(
    "INSERT INTO student (FIRST,LAST,AGE,EMAIL,ID)\
VALUES('Krupa','Shekhat',19,'21ce133@charusat.edu.in',4)"
)
c.execute(
    "INSERT INTO student (FIRST,LAST,AGE,EMAIL,ID)\
VALUES('Shruti','Sangani',19,'21ce118@charusat.edu.in',6)"
)
conn.commit()
print("Record created succesfully")

cursor = conn.execute("SELECT FIRST,LAST,AGE,EMAIL,ID from student;")

for row in cursor:
    print("FIRST =", row[0])
    print("LAST =", row[1])
    print("AGE =", row[2])
    print("EMAIL =", row[3])
    print("ID =", row[4]), "\n"

print("Operation done Successfully")
conn.commit()
c.execute("UPDATE student set AGE =19 where ID=1")
conn.commit()
print("Update done Successfully")
c.execute("DELETE from student where ID = 1")
conn.commit()
print("Delete done Successfully")
conn.close()
