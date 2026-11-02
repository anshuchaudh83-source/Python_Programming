from file_handler import read_file, write_file, append_file

def customer_menu():
    while True:
        print("\n--- CUSTOMER ---")
        print("1. View Menu")
        print("2. Order Food")
        print("3. Delete Order")
        print("4. View Orders")
        print("5. Feedback")
        print("6. Logout")

        c = input("Choice: ")

        if c == "1":
            view_menu()
        elif c == "2":
            order_food()
        elif c == "3":
            delete_order()
        elif c == "4":
            view_orders()
        elif c == "5":
            feedback()
        elif c == "6":
            break

def view_menu():
    items = read_file("menu.txt")
    for i in items:
        print(i.strip())

def order_food():
    name = input("Food: ")
    price = input("Price: ")

    append_file("orders.txt", f"{name},Pending,{price}")

def delete_order():
    orders = read_file("orders.txt")
    name = input("Food to delete: ")

    new = []
    for o in orders:
        if not o.startswith(name + ","):
            new.append(o)

    write_file("orders.txt", new)

def view_orders():
    orders = read_file("orders.txt")
    for o in orders:
        print(o.strip())

def feedback():
    fb = input("Feedback: ")
    append_file("feedback.txt", fb)