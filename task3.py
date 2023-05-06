class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.__private_attribute = breed

    def take_cat(self):
        self.__scare_cat()
        return "You took cat"

    def __scare_cat(self):
        print("You scared cat")


cat1 = Cat("Roxy", "British")
print(cat1.take_cat())
