USER_FILE = "data/users.txt"

def register_user():
    enrollment = input("Enrollment: ")
    password = input("Password: ")
    name = input("Name: ")
    email = input("Email: ")
    branch = input("Branch: ")
    year = input("Year: ")
    contact = input("Contact: ")
    usertype = "student"
    with open(USER_FILE, "a") as f:
        f.write(f"{enrollment},{password},{name},{email},{branch},{year},{contact},{usertype}\n")
    print("Registration successful!")
