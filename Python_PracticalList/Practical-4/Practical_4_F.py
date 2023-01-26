# Creating a function which calculates sum of list elements
def sumOfList(list):
    sum = 0
    for i in list:
        sum += int(i)

    return sum


# Taking length of list
n = int(input("\nEnter length of list:"))
print()
l = []

# Taking a list input from the user
for i in range(n):
    l.append(int(input("Enter number:")))

# Printing the sum of list elements
print("\nSum of list elements is", sumOfList(l), "\n")
