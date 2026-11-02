from file_handler import read_file

MAX_ATTEMPTS = 3

def login():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        print("\n===== LOGIN SYSTEM =====")

        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        users = read_file("users.txt")

        for user in users:
            data = user.strip().split(",")

            # safety check
            if len(data) < 3:
                continue

            file_user = data[0].strip()
            file_pass = data[1].strip()
            role = data[2].strip()

            if username == file_user and password == file_pass:
                print("Login Successful!")
                return role

        attempts += 1
        print("Invalid credentials! Attempts left:", MAX_ATTEMPTS - attempts)

    print("Too many failed attempts. Exiting system.")
    return None