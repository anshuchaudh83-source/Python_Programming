from file_handler import read_file, write_file, append_file

def chef_menu():
    while True:
        print("\n--- CHEF ---")
        print("1. View Orders")
        print("2. Update Order")
        print("3. Request Ingredient")
        print("4. Logout")

        c = input("Choice: ")

        if c == "1":
            view_orders()
        elif c == "2":
            update_order()
        elif c == "3":
            request_ingredient()
        elif c == "4":
            break

def view_orders():
    orders = read_file("orders.txt")
    for o in orders:
        print(o.strip())

def update_order():
    orders = read_file("orders.txt")
    name = input("Food name: ")

    new = []
    for o in orders:
        data = o.strip().split(",")
        if data[0] == name:
            status = input("Status: ")
            new.append(f"{data[0]},{status},{data[2]}\n")
        else:
            new.append(o)

    write_file("orders.txt", new)

def request_ingredient():
    name = input("Ingredient: ")
    qty = input("Quantity: ")

    append_file("ingredients.txt", f"{name},{qty},Requested")