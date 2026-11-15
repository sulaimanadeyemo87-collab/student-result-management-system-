from student import Student
from storage import load_students, save_students
from results import calculate_result, record_scores
from reports import show_all_results, show_student_report, show_class_statistics, save_text_report

DATA_FILE = "data/students.json"

def pause():
    input("\nPress Enter to continue...")

def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def add_student(students):
    student_id = read_non_empty("Student ID: ").upper()
    if student_id in students:
        print("That Student ID already exists.")
        return
    name = read_non_empty("Full name: ")
    student_class = read_non_empty("Class/Form: ")
    gender = read_non_empty("Gender: ")
    dob = read_non_empty("Date of birth (YYYY-MM-DD): ")
    student = Student(student_id, name, student_class, gender, dob)
    students[student_id] = student.to_dict()
    save_students(DATA_FILE, students)
    print("Student registered successfully.")

def list_students(students):
    if not students:
        print("No students registered yet.")
        return
    for item in students.values():
        print(f"{item['student_id']} | {item['full_name']} | {item['class_form']}")

def find_student(students):
    key = read_non_empty("Enter Student ID or part of name: ").lower()
    matches = [
        s for s in students.values()
        if key == s["student_id"].lower() or key in s["full_name"].lower()
    ]
    if not matches:
        print("No matching student found.")
    for s in matches:
        print(f"{s['student_id']} | {s['full_name']} | {s['class_form']}")

def update_student(students):
    sid = read_non_empty("Student ID to update: ").upper()
    if sid not in students:
        print("Student not found.")
        return
    s = students[sid]
    print("Leave a field blank to keep its current value.")
    for field, label in [
        ("full_name", "Full name"),
        ("class_form", "Class/Form"),
        ("gender", "Gender"),
        ("date_of_birth", "Date of birth")
    ]:
        value = input(f"{label} [{s[field]}]: ").strip()
        if value:
            s[field] = value
    save_students(DATA_FILE, students)
    print("Student information updated.")

def delete_student(students):
    sid = read_non_empty("Student ID to delete: ").upper()
    if sid not in students:
        print("Student not found.")
        return
    confirm = input(f"Delete {students[sid]['full_name']}? (y/n): ").lower()
    if confirm == "y":
        del students[sid]
        save_students(DATA_FILE, students)
        print("Student record deleted.")
    else:
        print("Deletion cancelled.")

def enter_or_update_scores(students):
    sid = read_non_empty("Student ID: ").upper()
    if sid not in students:
        print("Student not found.")
        return
    record_scores(students[sid])
    save_students(DATA_FILE, students)

def show_one_report(students):
    sid = read_non_empty("Student ID: ").upper()
    if sid not in students:
        print("Student not found.")
        return
    show_student_report(students[sid])

def menu():
    students = load_students(DATA_FILE)
    actions = {
        "1": lambda: add_student(students),
        "2": lambda: list_students(students),
        "3": lambda: find_student(students),
        "4": lambda: update_student(students),
        "5": lambda: delete_student(students),
        "6": lambda: enter_or_update_scores(students),
        "7": lambda: show_one_report(students),
        "8": lambda: show_all_results(students),
        "9": lambda: show_class_statistics(students),
        "10": lambda: save_text_report(students, "student_results_report.txt"),
    }
    while True:
        print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
        print("1. Register student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student information")
        print("5. Delete student")
        print("6. Enter/update subject scores")
        print("7. View individual report card")
        print("8. View all results (sorted by average)")
        print("9. View class statistics")
        print("10. Save text report to file")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            save_students(DATA_FILE, students)
            print("Data saved. Goodbye.")
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except (ValueError, KeyError) as error:
                print(f"Could not complete the operation: {error}")
        else:
            print("Invalid option. Choose from the menu.")

if __name__ == "__main__":
    menu()
