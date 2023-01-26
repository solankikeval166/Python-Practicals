# creating dictionary dict1,dict2 and dict3
dict1 = {
    "name": "Keval",
    "age": 18,
    "city": "Dhoraji",
    "country": "India"
}

dict2 = {
    "name": "Poorv",
    "age": 19,
    "city": "Dhoraji",
    "country": "India"
}

dict3 = {
    "name": "Mahek",
    "age": 20,
    "city": "Dhoraji",
    "country": "India"
}

# update will add key value pair in dict1
dict1.update({"Date of Birth": "30/03/04"})
print()
print("After Updating:", dict1)
print()

# del will remove key value pair from dict1
del dict1["country"]

print("After deleting country:", dict1)
print()

# clear will clear all items in dict1
dict1.clear()

print("After clear():", dict1)
print()

# popitem will remove last key value pair from dict2
dict2.popitem()

print("After popitem():", dict2)
print()

# pop will remove single key value pair from dict2
dict2.pop("city")

print("After pop():", dict2)
print()

# get will return value according to key in dict
print("Method get('name'):", dict2.get("name"))

# Merging three dictionary in dict1
dict4 = {
    "name": "Meera",
    "age": 20,
    "city": "Dhoraji",
    "country": "India"
}

dict5 = {
    "hobbies": "Badmintion",
    "skills": "Java,c++"
}

dict6 = {
    "education": "B.tech",
    "college": "Charusat",
    "school": "Royal Science School"
}

# Merging dictionaries
dict5.update(dict6)
dict4.update(dict5)

print()
print("After merging :", dict4)
print()
