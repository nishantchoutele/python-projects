def display_menu():
    print("\n--- Shopping List Manager  ---")
    print("1. ADD item")
    print("2. Remove item")
    print("3. View Shopping list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item name: ").strip() #stripe function removes whitespace
    is_essential = input("Is this item essential? (Yes/No): ").strip().lower() #Lower to convert char into lowercase

    if is_essential == 'yes':
        shopping_list["essential"].append(item)
    else:
        shopping_list["non_essential"].append(item)

    print(f"'{item}' has been added to your shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item name to remove:").strip()
    found = False #to track the item is in the list or not

    for category in shopping_list:
        if item in shopping_list[category]:
            shopping_list[category].remove(item)
            print(f"'{item}' has been removed from your shopping list")
            found = True
            break
        
    if not found:
        print(f"'{item}' was not found in your shopping list")

def view_list(shopping_list):
    print("\n---Your Shopping list ---")
    if all(len(items) == 0 for items in shopping_list.values()):
        print(" Your shopping list is empty.")
    else:
        for category, items in shopping_list.items():
            print(f"\n{category.capitalize()} items:")
            for index, item in enumerate(items, start=1):
                print(f"{index}.  {item}")

def main():
    shopping_list = {"essential":[], "non_essential":[]}
    while True:
        display_menu()

        choice = input("Choose the option 1-4:").strip()
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting Shopping list Manager.")
            break
        else:
            print("invalid choice! Please enter a valid Option")

if __name__ == "__main__":
    main()
