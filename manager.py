from file_handler import read_file, write_file, append_file

def manager_menu():
    while True:
        print("\n--- MANAGER ---")
        print("1. Add Menu")
        print("2. Edit Menu")
        print("3. Delete Menu")
        print("4. View Ingredients")
        print("5. Approve Ingredient")
        print("6. Logout")

        c = input("Choice: ")

        if c == "1":
            add_menu()
        elif c == "2":
            edit_menu()
        elif c == "3":
            delete_menu()
        elif c == "4":
            view_ingredients()
        elif c == "5":
            approve_ingredient()
        elif c == "6":
            break

def add_menu():
    name = input("Food: ")
    price = input("Price: ")

    if not price.isdigit():
        print("Invalid price!")
        return

    append_file("menu.txt", f"{name},{price}")

def edit_menu():
    items = read_file("menu.txt")
    name = input("Food to edit: ")

    new = []
    for item in items:
        data = item.strip().split(",")
        if data[0] == name:
            new_price = input("New price: ")
            new.append(f"{name},{new_price}\n")
        else:
            new.append(item)

    write_file("menu.txt", new)

def delete_menu():
    items = read_file("menu.txt")
    name = input("Food to delete: ")

    new = []
    for item in items:
        if not item.startswith(name + ","):
            new.append(item)

    write_file("menu.txt", new)

# INGREDIENT SYSTEM
def view_ingredients():
    data = read_file("ingredients.txt")
    for d in data:
        print(d.strip())

def approve_ingredient():
    items = read_file("ingredients.txt")
    name = input("Ingredient to approve: ")

    new = []
    for item in items:
        data = item.strip().split(",")
        if data[0] == name:
            new.append(f"{data[0]},{data[1]},Approved\n")
        else:
            new.append(item)

    write_file("ingredients.txt", new)