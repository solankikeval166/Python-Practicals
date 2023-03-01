class Parent:
    def _init_(self):
        print("Parent constructor called")

    def parent(self):
        print("Parent function called")


class Father:
    def father(self):
        print("Father function called")


class Mother:
    def mother(self):
        print("Mother function called")

# Child class


class Child(Parent):
    def _init_(self):
        super()._init_()

    def child(self):
        print("Child function called")


class Son(Mother, Father):
    def son(self):
        print("Son function called")


# Grandchild class


class Grandchild(Child):
    def _init_(self):
        super()._init_()

    def grandchild(self):
        print("Grandchild function called")


print("\nSingle level inheritance:")
person = Child()
person.child()

print("\nMulti level inheritance:")
person = Grandchild()
person.grandchild()

print("\nMultiple inheritance:")
person = Son()
person.son()
person.mother()
person.father()


