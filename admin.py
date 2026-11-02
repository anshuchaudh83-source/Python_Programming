from file_handler import read_file, write_file, append_file

def admin_menu():
    while True:
        print("\n--- ADMIN ---")
        print("1. Add Staff")
        print("2. Delete Staff")
        print("3. View Feedback")
        print("4. Sales Report")
        print("5. Logout")

        c = input("Choice: ")

        if c == "1":
            add_staff()
        elif c == "2":
            delete_staff()
        elif c == "3":
            view_feedback()
        elif c == "4":
            sales_report()
        elif c == "5":
            break

def add_staff():
    u = input("Username: ")
    p = input("Password: ")
    r = input("Role (manager/chef): ")

    append_file("users.txt", f"{u},{p},{r}")
    print("Staff added!")

def delete_staff():
    users = read_file("users.txt")
    u = input("Username to delete: ")

    new = []
    for user in users:
        if not user.startswith(u + ","):
            new.append(user)

    write_file("users.txt", new)
    print("Staff deleted!")

def view_feedback():
    data = read_file("feedback.txt")
    for d in data:
        print(d.strip())

def sales_report():
    orders = read_file("orders.txt")
    total = 0

    for o in orders:
        data = o.strip().split(",")
        if len(data) >= 3:
            total += int(data[2])

    print("Total Sales:", total)