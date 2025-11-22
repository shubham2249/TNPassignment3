score_file = "data/scores.txt"
import random, datetime
USER_FILE = "data/users.txt"

def load_questions(filename):
    with open(filename, "r") as f:
        content = f.read().strip().split("\n\n")
    questions = []
    for q in content:
        lines = q.strip().split("\n")
        ques = lines[0]
        options = lines[1:5]
        answer = lines[5].split(":")[1].strip()
        questions.append((ques, options, answer))
    return questions

def attempt_quiz(enrollment, category):
    filename = f"data/{category.lower()}.txt"
    questions = load_questions(filename)
    random.shuffle(questions)
    score = 0
    for i, (ques, options, ans) in enumerate(questions[:5], start=1):
        print(f"\nQ{i}. {ques}")
        for opt in options:
            print(opt)
        user_ans = input("Your answer (a/b/c/d): ").lower()
        if user_ans == ans:
            score += 1
    print(f"\nYour Score: {score}/{len(questions[:5])}")
    with open("data/scores.txt", "a") as f:
        f.write(f"{enrollment},{category},{score},{len(questions[:5])},{datetime.datetime.now()}\n")

def show_scores(enrollment):
    print("\n--- Your Scores ---")
    with open(score_file, "r") as f:
        for line in f:
            e, cat, sc, total, dt = line.strip().split(",")
            if e == enrollment:
                print(f"Category: {cat} | Score: {sc}/{total} | Date: {dt}")
def start_quiz(enrollment):
    while True:
        print("\nSelect Category:")
        print("1. DSA\n2. DBMS\n3. PYTHON\n4. SHOW_SCORE\n5. Logout")
        ch = input("Choice: ")
        if ch == '1':
            attempt_quiz(enrollment, "DSA")
        elif ch == '2':
            attempt_quiz(enrollment, "DBMS")
        elif ch == '3':
            attempt_quiz(enrollment, "PYTHON")
        elif ch == '4':
            show_scores(enrollment)
        elif ch == '5':
            print("Logged out.\n")
            break
        else:
            print("Invalid choice!")


