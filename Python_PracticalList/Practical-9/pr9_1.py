fodd = open("odd.txt", "a")

feven = open("even.txt", "a")

num = eval(input("Enter number : "))

if num % 2 == 0:
    print(num, "is even number.", file=feven)
    print("Number saved to even.txt")
else:
    print(num, "is odd number.", file=fodd)
    print("Number saved to odd.txt")

fodd.close()
feven.close()
