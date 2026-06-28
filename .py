from password_checker import check_password
from password_generator import generate_password

while True:
    print("\n==============================")
    print(" PASSWORD STRENGTH CHECKER")
    print("==============================")
    print("1. Check Password")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = input("Enter your password: ")
        check_password(password)

    elif choice == "2":
        print("\nGenerated Password:", generate_password())

    elif choice == "3":
        print("Thank you for using Password Strength Checker.")
        break

    else:
        print("Invalid Choice! Try Again.")