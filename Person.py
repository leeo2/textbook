
class Person:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def description(self):
        return "The name of the person is " + self.first_name + " " + self.last_name

    def birthday(self):
        self.age = self.age + 1
        return self.age
