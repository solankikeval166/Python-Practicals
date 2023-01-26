# declaration of lambda function
Square= lambda x:x*x

#declaration of square function
def squareOfList(list):
    for i in range(5):
        list[i] = Square(list[i])

    return l

l = []

#taking list input 
for i in range(5):
    l.append(int(input("Enter a number:")))
    
    
print("\nList:",l,"\n")
print("New list:",squareOfList(l),"\n")
