from typing import Optional, Dict

def add_item(items: Dict[str, float]) -> Optional[str]:
    name = input("Item name: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    if name in items:
        print("Item already exists.")
        return

    try:
        price = float(input(f"Price of {name}: "))
        if price < 0:
            print("Price cannot be negative.")
            return
    except ValueError:
        print("Invalid price.")
        return

    items[name] = price
    print(f"{name} added for {price}€.")


def edit_item(items: Dict[str, float]) -> Optional[str]:
    name = input("Which item do you want to edit? ").strip()

    if name not in items:
        print("Item not found.")
        return

    choice = input("Edit (1) name or (2) price? ")

    if choice == "1":
        new_name = input("New item name: ").strip()
        if not new_name:
            print("Name cannot be empty.")
            return
        items[new_name] = items.pop(name)
        print("Item renamed.")

    elif choice == "2":
        try:
            new_price = float(input("New price: "))
            if new_price < 0:
                print("Price cannot be negative.")
                return
            items[name] = new_price
            print("Price updated.")
        except ValueError:
            print("Invalid price.")


def delete_item(items):
    name = input("Item to delete: ").strip()

    if name not in items:
        print("Item not found.")
        return

    confirm = input(f"Delete {name} ({items[name]}€)? yes/no: ").lower()
    if confirm == "yes":
        del items[name]
        print("Item deleted.")
    else:
        print("Item not deleted.")


def show_items(items):
    if not items:
        print("Your shopping list is empty.")
        return

    print("Your shopping list:")
    for name, price in items.items():
        print(f"- {name}: {price}€")


def checkout(items):
    total = sum(items.values())
    print(f"Your total is {total}€.")
    print("Thank you for shopping!")


def main() -> None:
    items = {}
    print("Hello dear customer!")

    while True:
        try:
            choice = input(
                "\nChoose an option:\n"
                "1. Add item\n"
                "2. Edit item\n"
                "3. Delete item\n"
                "4. Show shopping list\n"
                "5. Pay and exit\n"
            )
        except KeyboardInterrupt:
            print("\nExiting program.")
            break

        if choice == "1":
            add_item(items)
        elif choice == "2":
            edit_item(items)
        elif choice == "3":
            delete_item(items)
        elif choice == "4":
            show_items(items)
        elif choice == "5":
            checkout(items)
            break
        else:
            print("Please choose a number between 1 and 5.")


main()