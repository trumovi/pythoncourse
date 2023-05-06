class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

    def print_params(self):
        pass


class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def print_params(self):
        print("This is an oval with width", self.width, "and height", self.height, "and color", self.color)


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def print_params(self):
        print("This is a square with side", self.side, "and color", self.color)


oval = Oval(26, 14)
square = Square(23)

oval.change_color("black")
square.change_color("maroon")

oval.print_params()
square.print_params()