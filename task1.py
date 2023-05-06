class Cat:
    def __init__(self, color, name):
        self.color = color
        self.name = name


class Dog:
    def __init__(self, color, name):
        self._color = color
        self._name = name

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value


class Rabbit:
    def __init__(self, color, name):
        self.__color = color
        self.__name = name

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value


cat1 = Cat("gray", "Roxy")
print(cat1.name)
cat1.name = "Biscuit"
print(cat1.name)

dod1 = Dog("brown", "Harry")
print(dod1.get_color())
dod1.set_color("black")
print(dod1.get_color())

rabbit1 = Rabbit("white", "Millie")
print(rabbit1.get_color())
rabbit1.set_color("red")
print(rabbit1.get_color())
print(rabbit1.__color)  # AttributeError: 'Rabbit' object has no attribute '__color'.