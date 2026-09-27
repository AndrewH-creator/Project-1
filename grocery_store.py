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


def remove_grocery(groceries):
    """Remove a grocery item selected by the user."""
    if not groceries:
        print("There are no grocery items to remove.")
        return

    display_groceries(groceries)

    choice = input("Enter the number of the item to remove: ")

    if choice.isdigit():
        item_number = int(choice)

        if 1 <= item_number <= len(groceries):
            removed_item = groceries.pop(item_number - 1)
            print(f"{removed_item['name']} was removed.")
        else:
            print("That item number does not exist.")
    else:
        print("Please enter a valid number.")


def mark_purchased(groceries):
    """Mark a selected grocery item as purchased."""
    if not groceries:
        print("There are no grocery items.")
        return

    display_groceries(groceries)

    choice = input("Enter the number of the purchased item: ")

    if choice.isdigit():
        item_number = int(choice)

        if 1 <= item_number <= len(groceries):
            groceries[item_number - 1]["purchased"] = True
            print("Item marked as purchased.")
        else:
            print("That item number does not exist.")
    else:
        print("Please enter a valid number.")


def calculate_total(groceries):
    """Calculate and display the estimated cost of all groceries."""
    total = 0

    for item in groceries:
        total += item["price"]

    print(f"Estimated grocery total: ${total:.2f}")


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
            remove_grocery(groceries)
        elif choice == "4":
            mark_purchased(groceries)
        elif choice == "5":
            calculate_total(groceries)
        elif choice == "6":
            running = False
            print("Thank you for using the Grocery Store Checklist!")
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
