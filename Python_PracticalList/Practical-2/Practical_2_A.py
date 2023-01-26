# Creation and initialization of list l
l = [1,5,2,3,4,9,6]

#Printing list l
print("list l:",l)

#append() will add a new element at the end of the list
l.append(8)
l.append(7)
print("Updated list after apend():",l)

#printing list l with for loop
# for i in l:
#     print(i)

#extend() method will add multiple elements in the list
l.extend([11,15,12,13])
print("Updated list after extend():",l)

#Remove() will remove specified element
l.remove(11)
l.remove(13)
l.remove(12)
l.remove(15)

print("Updated list after remove():",l)

#Reverse() will reverse all elements in list
l.reverse()
print("reverse() the list:",l)

#Printing list in ascending order
l.sort()
print("Ascending order:",l)

#Printing list in descending order
l.sort(reverse=True)
print("Descending order:",l)