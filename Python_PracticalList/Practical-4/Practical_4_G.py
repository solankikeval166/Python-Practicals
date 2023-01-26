# Declaring a comprehensive
def comprehension():
    ListOfEven = []
    ListOfOdd = []
    List = []

    # seprating even and odd numbers
    for i in range(1, 51):
        if i % 2 == 0:
            ListOfEven.append(i)
        else:
            ListOfOdd.append(i)

    for i in range(1, 101):
        if i % 5 == 0:
            List.append(i)

    return ListOfEven, ListOfOdd, List


l1, l2, l3 = comprehension()

# Printing list items.
print("\nEven List:", l1, "\n\nOdd List:", l2, "\n\nList:", l3, "\n")