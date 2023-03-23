import MySQLdb 

# Open database connection 
db = MySQLdb.connect("localhost","root","","mydatabase" ) 

# prepare a cursor object using cursor() method 
cursor = db.cursor() 
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000) 

try: 
      # Execute the SQL command 
      cursor.execute(sql) 

      # Fetch all the rows in a list of lists. 
      results = cursor.fetchall() 
      for row in results: 
          fname = row[0] 
          lname = row[1] 
          age = row[2] 
          Gender = row[3] 
          income = row[4]     
# Now print fetched result 
          print("fname={0} , lname={1} age={2} Gender={3} income={4}".format(fname,lname,age,Gender,income))
except: 
      print ("Error: unable to fecth data" )

# disconnect from server 
db.close() 
