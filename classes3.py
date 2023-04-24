class Box:
    def __init__(self, name):
        self.name = name
        self.figures = []

    def put(self, figure):
        self.figures.append(figure)
        print(f"You are put {figure.name} in {self.name}")

    def inbox(self):
        print(f"Box \"{self.name}\" has:")
        for figure in self.figures:
            figure.desc()

class Figure:
    name = None

    def __init__(self, color):
        self.color = color

    def desc(self):
        print(self.color, self.name)


class Square(Figure):
    name = "square"

    def __init__(self, color, side):
        self.side = side
        super().__init__(color)


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, color, a, b):
        self.a = a
        self.b = b
        super().__init__(color)


class Circle(Figure):
    name = "circle"

    def __init__(self, color, radius):
        self.radius = radius
        super().__init__(color)


box1 = Box("Kid's")
f1 = Rectangle("pink", 20, 10)
f2 = Circle("red", 15)

box1.put(f1)
box1.put(f2)
box1.inbox()