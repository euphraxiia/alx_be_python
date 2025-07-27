def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # This is the array/list

    while True:
        display_menu()  # Calling the function

        try:
            choice = int(input("Enter your choice: "))  # Choice input as a number
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added.")
        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == 3:
            print("Current Shopping List:")
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
