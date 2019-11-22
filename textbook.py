# Olivia Lee
# 11-20-19

from Person import Person

class Textbook:


    def __init__(self, title, first, last, age, edition, ISBN, publisher, year_published, quantity_in_inventory, price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.ISBN = ISBN
        self.publisher = publisher
        self.year_published = year_published
        self.quantity_in_inventory = quantity_in_inventory
        self.price = price

    def description(self):
        return self.title + "by" + self.author + "is the" + self.edition + "edition with an ISBN of" + self.ISBN + ". It was published in" + self.year_published + "by" + self.publisher + ". There are" + self.quantity_in_inventory + "in our inventory currently selling for $" + self.price



    def add_inventory(self, addition):
        self.quantity_in_inventory = self.quantity_in_inventory + int(addition)

    def decrease_inventory(self, loss):
        self.quantity_in_inventory = self.quantity_in_inventory - int(loss)


