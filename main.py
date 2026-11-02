from auth import login
from admin import admin_menu
from manager import manager_menu
from chef import chef_menu
from customer import customer_menu

def main():
    role = login()
    if role == "admin":
        admin_menu()
    elif role == "manager":
        manager_menu()
    elif role == "chef":
        chef_menu()
    elif role == "customer":
        customer_menu()
    else:
        print("Exit system")

main()