from results import calculate_result

def show_student_report(student):
    result = calculate_result(student)
    print("\n========== STUDENT REPORT CARD ==========")
    print(f"Student ID: {student['student_id']}")
    print(f"Name: {student['full_name']}")
    print(f"Class/Form: {student['class_form']}")
    print(f"Gender: {student['gender']}")
    print(f"Date of Birth: {student['date_of_birth']}")
    print("-----------------------------------------")
    if student.get("scores"):
        for subject, score in student["scores"].items():
            entered = student.get("score_dates", {}).get(subject, "Not recorded")
            print(f"{subject}: {score:g}  (entered: {entered})")
    else:
        print("No scores have been entered.")
    print("-----------------------------------------")
    print(f"Total: {result['total']:.2f}")
    print(f"Average: {result['average']:.2f}")
    print(f"Grade: {result['grade']}")
    print("=========================================")

def show_all_results(students):
    rows = []
    for student in students.values():
        result = calculate_result(student)
        rows.append((student["full_name"], student["student_id"], result))
    rows.sort(key=lambda row: row[2]["average"], reverse=True)
    if not rows:
        print("No student results available.")
        return
    print("\nNAME | STUDENT ID | TOTAL | AVERAGE | GRADE")
    for name, sid, result in rows:
        print(f"{name} | {sid} | {result['total']:.2f} | {result['average']:.2f} | {result['grade']}")

def show_class_statistics(students):
    averages = [
        calculate_result(s)["average"]
        for s in students.values()
        if s.get("scores")
    ]
    if not averages:
        print("No scores available for class statistics.")
        return
    print(f"Highest average: {max(averages):.2f}")
    print(f"Lowest average: {min(averages):.2f}")
    print(f"Class average: {sum(averages) / len(averages):.2f}")

def save_text_report(students, file_path):
    rows = []
    for student in students.values():
        result = calculate_result(student)
        rows.append((student["full_name"], student["student_id"], result))
    rows.sort(key=lambda row: row[2]["average"], reverse=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("STUDENT RESULT MANAGEMENT SYSTEM\n")
        file.write("=================================\n")
        for name, sid, result in rows:
            file.write(
                f"{name} | {sid} | Total: {result['total']:.2f} | "
                f"Average: {result['average']:.2f} | Grade: {result['grade']}\n"
            )
    print(f"Text report saved as {file_path}")
