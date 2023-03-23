import MySQLdb 


db = MySQLdb.connect("localhost","root","","mydatabase" ) 

# prepare a cursor object using cursor() method 
cursor = db.cursor() 

cursor.execute("SELECT VERSION()") 

data = cursor.fetchone() 

print ("Database version : %s " % data )

# disconnect from server 
db.close() 
