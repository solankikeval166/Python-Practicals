# defining the function table
def printTable(number):

    for i in range(1, 11):
        print(number, " x ",i, " = ",(number*i))

#Taking input from user
n = int(input("Table of number: "))

#printing table of inputted number
printTable(n)
