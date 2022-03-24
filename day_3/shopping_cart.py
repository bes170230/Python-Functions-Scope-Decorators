### 1) Build a Shopping Cart <br>
# You can use either lists or dictionaries. The program should have the following capabilities:
# 1) Takes in input
# 2) Stores user input into a dictionary or list 
# 3) The User can add or delete items 
# 4) The User can see current shopping list 
# 5) The program Loops until user 'quits' 
# 6) Upon quiting the program, print out all items in the user's list

shopping_list = []
while True:
    print("\nMenu:")
    print("1: Add item to list")
    print("2: Delete item from list")
    print("3: View list")
    print("4: Quit")
    selection = input("Please enter a selection, 1-4: ")
    selection = int(selection)
    if selection == 1:
        item_to_add = input("Please enter the name of the item you'd like to add to your cart: ")
        if item_to_add.title() in shopping_list:
                print("\nError: That item is already on the list.")
        else:
            shopping_list.append(item_to_add.title())
    elif selection == 2:
        item_to_delete = input("Please enter the name of the item you'd like to delete: ")
        if item_to_delete.title() in shopping_list:
            while item_to_delete.title() in shopping_list:
                shopping_list.remove(item_to_delete.title())
            print("\nDeleted " + item_to_delete)
        else:
            print("\nThat item is not currently in the list.")
    elif selection == 3:
        print("\nCurrent list contents: ")
        if shopping_list == []:
            print("The list is empty.\n")
        for item in shopping_list:
            print(item)
    elif selection == 4:
        print(f"\nList contents: {shopping_list}")
        print("Goodbye!")
        break
    else:
        print("\nInvalid selection. Please try again.")
        
