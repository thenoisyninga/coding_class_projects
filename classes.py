currentYear = 2022


class Person:
    def __init__(self, nameP, ageP):
        self.__name = nameP
        self.__age = ageP

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName


x = Person(nameP="Bob", ageP=17)
print(x.getName())
x.setName("John")
print(x.getName())



