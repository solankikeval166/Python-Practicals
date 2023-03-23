import MySQLdb 

# Open database connection 
db = MySQLdb.connect("localhost","root","","mydatabase" ) 

# prepare a cursor object using cursor() method 
cursor = db.cursor() 

# Prepare SQL query to UPDATE required records 
sql = "UPDATE EMPLOYEE SET INCOME=35000 WHERE GENDER = 'M' "
#adding 8000 in priti's income
try: 
       # Execute the SQL command 
       cursor.execute(sql) 

       # Commit your changes in the database 
       db.commit() 
except: 
       # Rollback in case there is any error 
       db.rollback() 

# disconnect from server 
db.close() 
