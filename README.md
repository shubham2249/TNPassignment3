 ## Quiz Management System (Python – File Handling Based)

A simple and interactive Quiz Application implemented in Python, using only File Handling (no database).
Supports User & Admin login, MCQ quizzes, score tracking, and profile management.

**Features**

1. User & Admin Authentication

2. User Registration

3. User Login

4. Admin Login (predefined – no registration)

5. Separate dashboard for Users and Admin.

**Quiz Module**

✔ Categories Supported

1. DSA

2. DBMS

3. PYTHON

(Questions are stored in separate files like dsa.txt, dbms.txt, python.txt)

✔ Attempt Quiz

1. Choose a category

2. Loads questions from file

3. Randomly shuffles questions

4. Shows 5–10 questions

5. One question at a time

MCQ format

🧮 Score System

After quiz completion, the system stores results inside scores.txt.

Each entry includes:

Enrollment Number

Category

Marks (e.g., 7/10)

Date & Time

Example:

20231045 | PYTHON | 8/10 | 2025-02-18 15:42

👤 User Profile Management

Users can:

View profile

Update profile (name, email, branch, year, contact)

Update password

View their quiz history

Stored in: users.txt

🛠 Admin Features

Admin can:

View all registered users

View all quiz scores

Add questions to categories

Manage category files

📂 Project File Structure
📁 Quiz-Management-System/
│
├── main.py
├── users.txt
├── scores.txt
├── admin.txt
│
├── dsa.txt
├── dbms.txt
├── python.txt
│
└── README.md

▶️ How to Run

Install Python 3

Clone this repo:

git clone https://github.com/shubham2249/TNPassignment3.git


Navigate into folder:

cd Quiz-Management-System


Run the program:

python main.py

📌 Technologies Used

Python

File Handling

Random Module

Datetime Module

🚀 Future Enhancements

Add timer for answering questions

Add more quiz categories

Add leaderboard

Convert to SQLite or MySQL version

Add GUI via Tkinter or Web UI (Flask)
