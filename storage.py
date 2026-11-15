import json
import os

def load_students(file_path):
    try:
        if not os.path.exists(file_path):
            return {}
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: Could not load saved data: {error}")
        return {}

def save_students(file_path, students):
    folder = os.path.dirname(file_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)
