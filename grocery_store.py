"""Grocery Store Checklist.

Author: Andrew Hissong
Purpose: Create a grocery store checklist program that demonstrates
         Python concepts from Chapters 1-7 of Python Crash Course.
Starter Code/Resources: No starter code used.
Date: September 27, 2026
"""


def display_groceries(groceries):
    """Display all grocery items and their information."""
    print("\nGrocery List")
    print("-" * 40)

    for number, item in enumerate(groceries, start=1):
        status = "Purchased" if item["purchased"] else "Not Purchased"

        print(
            f"{number}. {item['name']} | "
            f"{item['category']} | "
            f"${item['price']:.2f} | "
            f"{status}"
        )


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
    display_groceries(groceries)


if __name__ == "__main__":
    main()
