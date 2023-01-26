# Taking Principal amount from user
p = int(input("Enter the Principal amount: ")) 

#Taking Rate of Interest from user
r = int(input("Enter the rate: "))

#Taking number of years from user
n = int(input("Number of years: "))

#Calculating simple interest rate 
i = (p*r*n)/100

#Printing the simple interest rate
print("Simple Interest for given data is: " , i)