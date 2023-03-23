import MySQLdb 

# Open database connection 
db = MySQLdb.connect("localhost","root","","mydatabase" ) 

# prepare a cursor object using cursor() method 
cursor = db.cursor() 

# Prepare SQL query to INSERT a record into the database. 
sql="INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME, AGE, GENDER, INCOME) VALUES ('Ishita', 'Vachhani', 24, 'F', 38000)"


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
