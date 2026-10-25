"""
functions.py
Reusable calculation / processing functions for the
Student Performance Analytics System.
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------
# Project settings (grading rule and pass condition)
# ---------------------------------------------------------------
SUBJECTS = ["Python", "Mathematics", "Physics", "Electronics", "English"]
PASS_MARK = 40            # a student must score at least this in EVERY subject
ATTENDANCE_LIMIT = 75     # attendance below this (%) is flagged as a shortage

# Grading rule based on the average marks: (minimum average, grade)
GRADE_RULES = [
    (90, "A+"),
    (80, "A"),
    (70, "B+"),
    (60, "B"),
    (50, "C"),
    (40, "D"),
]


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df, subjects=SUBJECTS):
    """Add Total and Average columns for every student using NumPy."""
    marks = df[subjects].to_numpy()                 # 2D NumPy array of marks
    df["Total"] = np.sum(marks, axis=1)             # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)  # row-wise average
    return df


def assign_grade(average):
    """Return a grade for one average value using GRADE_RULES."""
    for minimum, grade in GRADE_RULES:
        if average >= minimum:
            return grade
    return "F"


def get_result(row_marks):
    """Return 'Pass' if every subject mark >= PASS_MARK, else 'Fail'."""
    if np.all(np.array(row_marks) >= PASS_MARK):
        return "Pass"
    return "Fail"


def add_grade_and_result(df, subjects=SUBJECTS):
    """Add Result, Grade and Attendance_Status columns (uses a loop)."""
    results = []
    grades = []
    attendance_status = []

    # Loop over every student row
    for _, row in df.iterrows():
        result = get_result(row[subjects].values)
        # A student who fails any subject gets grade F
        grade = assign_grade(row["Average"]) if result == "Pass" else "F"

        results.append(result)
        grades.append(grade)
        attendance_status.append(
            "OK" if row["Attendance"] >= ATTENDANCE_LIMIT else "Shortage"
        )

    df["Result"] = results
    df["Grade"] = grades
    df["Attendance_Status"] = attendance_status
    return df


def class_statistics(df):
    """Return overall class statistics as a dictionary."""
    averages = df["Average"].to_numpy()
    top = df.loc[df["Average"].idxmax()]
    low = df.loc[df["Average"].idxmin()]
    return {
        "Total students": len(df),
        "Class average": round(float(np.mean(averages)), 2),
        "Median average": round(float(np.median(averages)), 2),
        "Standard deviation": round(float(np.std(averages)), 2),
        "Highest average": float(top["Average"]),
        "Highest scorer": top["Name"],
        "Lowest average": float(low["Average"]),
        "Lowest scorer": low["Name"],
        "Average attendance": round(float(df["Attendance"].mean()), 2),
    }


def pass_fail_statistics(df):
    """Return pass count, fail count and pass percentage."""
    passed = int((df["Result"] == "Pass").sum())
    failed = int((df["Result"] == "Fail").sum())
    percentage = round(passed / len(df) * 100, 2)
    return passed, failed, percentage


def subject_analysis(df, subjects=SUBJECTS):
    """Return a DataFrame with highest, lowest, average and pass rate per subject."""
    rows = []
    for subject in subjects:                         # loop over subjects
        marks = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(marks)), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks)),
            "Pass %": round(float(np.sum(marks >= PASS_MARK) / len(marks) * 100), 1),
        })
    return pd.DataFrame(rows).sort_values("Average", ascending=False).reset_index(drop=True)


def top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    top = df.sort_values("Average", ascending=False).head(n).copy()
    top.insert(0, "Rank", range(1, len(top) + 1))
    return top[["Rank", "Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def department_analysis(df):
    """Return the average marks, attendance and pass count for each department."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)
    return summary.sort_values("Avg_Marks", ascending=False)


def grade_distribution(df):
    """Return the number of students for each grade."""
    order = ["A+", "A", "B+", "B", "C", "D", "F"]
    counts = df["Grade"].value_counts()
    return counts.reindex(order, fill_value=0)
