import MySQLdb 

# Open database connection 
db = MySQLdb.connect("localhost","root","","mydatabase" ) 

# prepare a cursor object using cursor() method 
cursor = db.cursor() 

sql = "DELETE FROM EMPLOYEE WHERE GENDER='M' "

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
