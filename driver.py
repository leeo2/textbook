# Olivia Lee

from textbook import Textbook

print("Textbook 1: ")
textbook_1 = Textbook(input("Title: "), input("Authors first name: "), input("Authors last name: "), int(input("Authors age: ")), int(input("Edition: ")), int(input("ISBN number: ")), input("Publisher: "), int(input("Year published: ")), int(input("Quantity in stock: ")), float(input("Price: ")), )
print("Textbook 2: ")
textbook_2 = Textbook(input("Title: "), input("Authors first name: "), input("Authors last name: "), int(input("Authors age: ")), int(input("Edition: ")), int(input("ISBN number: ")), input("Publisher: "), int(input("Year published: ")), int(input("Quantity in stock: ")), float(input("Price: ")), )

menu_choice = 0
again_choice = 1


print(f"Would you like to view 1. {textbook_1.title} or 2. {textbook_2.title}. Please enter a 1 or a 2.")
book_choice = int(input("> "))


while again_choice == 1:
    if book_choice == 1:

        while menu_choice != 4:
            print("Please chose the number to indicate which option you would like to choose")
            print("1. Add inventory")
            print("2. Decrease inventory")
            print("3. Change price")
            print("4. Leave everything how it is")

            menu_choice = int(input("> "))

            if menu_choice == 1:
                print("You chose to add inventory")
                addition = input("How many books did we add: ")
                textbook_1.add_inventory(addition)
                print(textbook_1.quantity_in_inventory)
            elif menu_choice == 2:
                print("You chose to decrease inventory")
                lose = input("How many books did we sell: ")
                textbook_1.decrease_inventory(lose)
                print(textbook_1.quantity_in_inventory)
            elif menu_choice == 3:
                print("You chose to change the price")
                print(f"The current price is: ${textbook_1.price}")
                textbook_1.price = float(input("The price is now: $"))
            elif menu_choice == 4:
                print("You chose to leave this book as it is.")
            else:
                print("Invalid choice")
    elif book_choice == 2:
        while menu_choice != 4:
            print("Please chose the number to indicate which option you would like to choose")
            print("1. Add inventory")
            print("2. Decrease inventory")
            print("3. Change price")
            print("4. Leave everything how it is")

            menu_choice = int(input("> "))

            if menu_choice == 1:
                print("You chose to add inventory")
                addition = input("How many books did we add: ")
                textbook_2.add_inventory(addition)
                print(textbook_2.quantity_in_inventory)
            elif menu_choice == 2:
                print("You chose to decrease inventory")
                lose = input("How many books did we sell: ")
                textbook_2.decrease_inventory(lose)
                print(textbook_2.quantity_in_inventory)
            elif menu_choice == 3:
                print("You chose to change the price")
                print(f"The current price is: ${textbook_2.price}")
                textbook_2.price = float(input("The price is now: $"))
            elif menu_choice == 4:
                print("You chose to leave this book as it is.")
            else:
                print("Invalid choice")
