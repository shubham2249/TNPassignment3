USER_FILE = 'data/users.txt'
from admin_dashboard import admin_panel
from user_dashboard import start_quiz

def login_user():

    enrollment = input("Enrollment: ").strip()
    password = input("Password: ").strip()

    if enrollment == 'admin' and password == 'password':
        print("\nWelcome, Admin!")
        admin_panel()
        return
    else:

        with open(USER_FILE, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                e, p, name, email, branch, year, contact, usertype = line.strip().split(',')
                if e == enrollment and p == password:
                    print(f"\nWelcome {name}!")
                    start_quiz(enrollment)
                    return
    print("Invalid credentials!")