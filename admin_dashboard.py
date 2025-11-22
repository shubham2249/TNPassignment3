import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def admin_panel():
    from user_dashboard import USER_FILE
    while True:
        print('\n=== ADMIN PANEL ===')
        print('1. View all users')
        print('2. View all scores')
        print('3. Add question to category')
        print('4. Back')
        choice = input('Choice: ').strip()
        if choice == '1':
            with open(USER_FILE, 'r', encoding='utf-8') as f:
                print('\nUsers:')
                for line in f:
                    if not line.strip():
                        continue
                    e, p, name, email, branch, year, contact, usertype = line.strip().split(',')
                    print(f"{e} | {name} | {email} | {branch} | {year} | {contact} | {usertype}")
        elif choice == '2':
            scores_path = os.path.join(DATA_DIR, 'scores.txt')
            with open(scores_path, 'r', encoding='utf-8') as f:
                print('\nScores:')
                for line in f:
                    if not line.strip():
                        continue
                    print(line.strip())
        elif choice == '3':
            print('\nChoose category to add question:')
            print('1. DSA\n2. DBMS\n3. PYTHON')
            c = input('Choice: ').strip()
            cat = None
            if c == '1':
                cat = 'dsa'
            elif c == '2':
                cat = 'dbms'
            elif c == '3':
                cat = 'python'
            else:
                print('Invalid')
                continue
            q = input('Enter question text: ').strip()
            a = input('Option a: ').strip()
            b = input('Option b: ').strip()
            c_opt = input('Option c: ').strip()
            d = input('Option d: ').strip()
            ans = input('Correct option (a/b/c/d): ').strip().lower()
            with open(os.path.join(DATA_DIR, f"{cat}.txt"), 'a', encoding='utf-8') as f:
                f.write(q + '\n')
                f.write(a + '\n')
                f.write(b + '\n')
                f.write(c_opt + '\n')
                f.write(d + '\n')
                f.write('Answer: ' + ans + '\n\n')
            print('Question added.')
        elif choice == '4':
            break
        else:
            print('Invalid')