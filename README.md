# Student Result Management System

A menu-driven student records and result application written in Python.

## Features
- Register, view, search, update and delete student records.
- Enter and update scores for at least five subjects.
- Calculate total, average and grade automatically.
- Display an individual report card.
- List results sorted from highest average to lowest.
- Calculate highest, lowest and class average.
- Save records in a JSON file and load them when the program starts.
- Export a simple text report.

## Requirements
- Python 3.8 or newer
- No third-party packages are required.

## How to run
1. Download or clone this repository.
2. Open a terminal in the `student_result_system` folder.
3. Run:

   ```bash
   python main.py
   ```

   On some computers, use `python3 main.py`.

## Data storage
Student records are stored in `data/students.json`. The program creates the data folder/file if needed. Back up this file before making major changes.

## Grading scale
The sample grading scale in `results.py` is:
- A: 80–100
- B: 70–79
- C: 60–69
- D: 50–59
- F: below 50

Change the boundaries in `grade_from_average()` if your lecturer or school specifies another scale.

## Important notes
- Enter scores from 0 to 100.
- Enter at least five subjects for each student's result.
- The date and time each subject score is entered are stored.
- This is a simple classroom project; test each menu option with sample records before submission.
