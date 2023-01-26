# declaration of findMax function
def findMax(a, b):

    if a < b:
        return b
    else:
        return a


for i in range(5):
    print()
    # taking multiple input using split
    x, y, z = (input("Enter three nubers:").split())

    # Printing the maximum value
    print("Maximum Number is :", findMax(x, findMax(y, z)))