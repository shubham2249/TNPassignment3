from register import register_user
from login import login_user


def main():
    while True:
        print("\n=== QUIZ APP ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        ch = input("Enter choice: ")

        if ch == '1':
            register_user()
        elif ch == '2':
            login_user()
        elif ch == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()