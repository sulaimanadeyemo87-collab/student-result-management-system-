from datetime import datetime

# Edit these grade boundaries if your school uses a different grading scale.
def grade_from_average(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"

def calculate_result(student):
    scores = student.get("scores", {})
    if not scores:
        return {"total": 0, "average": 0, "grade": "N/A"}
    total = sum(scores.values())
    average = total / len(scores)
    return {
        "total": total,
        "average": round(average, 2),
        "grade": grade_from_average(average)
    }

def record_scores(student):
    subjects = student.setdefault("scores", {})
    dates = student.setdefault("score_dates", {})
    print("Enter at least five subjects. Type DONE as a subject name when finished.")
    while True:
        subject = input("Subject name: ").strip()
        if subject.upper() == "DONE":
            if len(subjects) < 5:
                print("At least five subjects are required.")
                continue
            break
        if not subject:
            print("Subject name cannot be empty.")
            continue
        try:
            score = float(input(f"Score for {subject} (0-100): "))
            if not 0 <= score <= 100:
                print("Score must be between 0 and 100.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        subjects[subject] = score
        dates[subject] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{subject} saved.")
    result = calculate_result(student)
    print(f"Total: {result['total']:.2f} | Average: {result['average']:.2f} | Grade: {result['grade']}")
