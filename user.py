users = []

def generate_username(name):
    # Remove spaces and convert to lowercase
    clean_name = name.replace(" ", "").lower()

    # Generate username based on number of existing users
    username = clean_name + str(len(users) + 1)

    return username


def register_user():
    First_name = input("First name: ")
    Last_name = input("Last Name:")
    name = First_name + Last_name
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    phone = input("Phone Number: ")
    Gender = input("Gender: ")
    Address = input("Address/City: ")
    

    username = generate_username(name)

    user = {
        "name": name,
        "username": username,
        "email": email,
        "password": password,
        "phone": phone,
        "Gender": Gender,
        "Address": Address
    }

    users.append(user)

    print("\nRegistration successful!")
    print("Your generated username is:", username)


def display_users():
    if len(users) == 0:
        print("\nNo users registered yet.")
        return

    print("\nRegistered Users:")
    for user in users:
        print("----------------------")
        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("Phone Number: ",user["phone"])
        print("Gender: ",user["Gender"])
        print("Address: ",user["Address"])


while True:

    print("\n===== USER REGISTRATION SYSTEM =====")
    print("1. Register User")
    print("2. Display Users")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        display_users()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")