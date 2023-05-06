class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def print_info(self):
        print("Name:", self.name)
        print("Position:", self.position)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Manager", salary)

    def print_info(self):
        print("**** Manager ****")
        super().print_info()

class Journalist(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, "Journalist", salary)
        self.tool = tool

    def print_info(self):
        print("**** Journalist ****")
        super().print_info()
        print("Design tool:", self.tool)

class Translator(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, "Translator", salary)
        self.language = language

    def print_info(self):
        print("**** Translator ****")
        super().print_info()
        print("Language:", self.language)


class Photographer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, "Photographer", salary)
        self.tool = tool

    def print_info(self):
        print("**** Photographer ****")
        super().print_info()
        print("Design tool:", self.tool)


employees = [
    Manager("Mateusz Slodkowski", 50000),
    Translator("Petra Jaszapati", 60000, "Spanish"),
    Photographer("Matthew Stockman", 55000, "Photoshop"),
    Journalist("Geoff Robins", 61000, "Notebook")
]

for employee in employees:
    employee.print_info()
    print()