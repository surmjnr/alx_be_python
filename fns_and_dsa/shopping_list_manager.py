def display_menu():
    """Display the main menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Invalid input. Please enter a valid item name.")

def remove_item(shopping_list):
    """Remove an item from the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
        return
    
    print("Current items in your list:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
    
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' was not found in your shopping list.")

def view_list(shopping_list):
    """Display the current shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
