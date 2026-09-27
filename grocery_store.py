"""Grocery Store Checklist.

Author: Andrew Hissong
Purpose: Create a grocery store checklist program that demonstrates
         Python concepts from Chapters 1-7 of Python Crash Course.
Starter Code/Resources: No starter code used.
Date: September 27, 2026
"""


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
    print(f"There are currently {len(groceries)} items on your list.")


if __name__ == "__main__":
    main()
