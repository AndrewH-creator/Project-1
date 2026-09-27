"""Grocery Store Checklist.

Author: Andrew Hissong
Purpose: Create a grocery store checklist program that demonstrates
         Python concepts from Chapters 1-7 of Python Crash Course.
Starter Code/Resources: No starter code used.
Date: September 27, 2026
"""


def display_menu():
    """Display the available program choices."""
    print("\nMenu")
    print("1. View grocery list")
    print("2. Add grocery item")
    print("3. Remove grocery item")
    print("4. Mark item as purchased")
    print("5. View total cost")
    print("6. Quit")

def add_grocery(groceries):
    """Ask the user for information and add a grocery item."""
    name = input("Enter the grocery item name: ")
    category = input("Enter the grocery category: ")
    price = float(input("Enter the estimated price: "))

    grocery = {
        "name": name,
        "category": category,
        "price": price,
        "purchased": False
    }

    groceries.append(grocery)
    print(f"{name} was added to your grocery list.")


def main():
    """Run the Grocery Store Checklist program."""
    groceries = [
        {
            "name": "Milk",
            "category": "Dairy",
            "price": 3.49,
            "purchased": False
        },
        {
            "name": "Bread",
            "category": "Bakery",
            "price": 2.99,
            "purchased": False
        },
        {
            "name": "Apples",
            "category": "Produce",
            "price": 4.50,
            "purchased": False
        }
    ]

    print("Welcome to the Grocery Store Checklist!")

    running = True

    while running:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_groceries(groceries)
        elif choice == "2":
            add_grocery(groceries)
        elif choice == "3":
            print("Remove item selected.")
        elif choice == "4":
            print("Mark purchased selected.")
        elif choice == "5":
            print("View total selected.")
        elif choice == "6":
            running = False
            print("Thank you for using the Grocery Store Checklist!")
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
