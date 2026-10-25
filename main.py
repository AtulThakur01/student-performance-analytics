"""
main.py
Student Performance Analytics System
Runs the full analysis and prints the results.

Usage:  python main.py
"""

import os
import pandas as pd

import functions as fn

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student_results.csv")

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)


def heading(title):
    """Print a clean section heading."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # ---------------- Step 1 & 2: Load and inspect the data ----------------
    df = fn.load_data(DATA_FILE)

    heading("1. DATASET OVERVIEW")
    print(f"Number of records : {df.shape[0]}")
    print(f"Number of columns : {df.shape[1]}")
    print(f"Columns           : {list(df.columns)}")
    print(f"Missing values    : {int(df.isnull().sum().sum())}")
    print("\nFirst 5 records:")
    print(df.head().to_string(index=False))

    # ---------------- Step 3: Process the data ----------------
    df = fn.calculate_total_and_average(df)
    df = fn.add_grade_and_result(df)

    heading("2. STUDENT-WISE RESULT (Total, Average, Grade, Result)")
    result_cols = ["Student_ID", "Name", "Department", "Total", "Average",
                   "Grade", "Result", "Attendance", "Attendance_Status"]
    print(df[result_cols].to_string(index=False))

    # ---------------- Step 4: Analysis ----------------
    heading("3. CLASS PERFORMANCE SUMMARY")
    for key, value in fn.class_statistics(df).items():
        print(f"{key:<20}: {value}")

    heading("4. PASS / FAIL STATISTICS")
    passed, failed, percentage = fn.pass_fail_statistics(df)
    print(f"Passed          : {passed}")
    print(f"Failed          : {failed}")
    print(f"Pass percentage : {percentage}%")
    print(f"(Pass rule: at least {fn.PASS_MARK} marks in every subject)")
    print("\nFailed students:")
    print(df[df["Result"] == "Fail"][["Student_ID", "Name", "Average"]].to_string(index=False))

    heading("5. GRADE DISTRIBUTION")
    print(fn.grade_distribution(df).to_string())

    heading("6. SUBJECT-WISE PERFORMANCE (best subject first)")
    subject_table = fn.subject_analysis(df)
    print(subject_table.to_string(index=False))
    print(f"\nBest subject  : {subject_table.iloc[0]['Subject']} "
          f"(average {subject_table.iloc[0]['Average']})")
    print(f"Weakest subject: {subject_table.iloc[-1]['Subject']} "
          f"(average {subject_table.iloc[-1]['Average']})")

    heading("7. TOP 5 PERFORMING STUDENTS")
    print(fn.top_performers(df, 5).to_string(index=False))

    heading("8. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df).to_string())

    heading("9. ATTENDANCE ALERT (below 75%)")
    shortage = df[df["Attendance_Status"] == "Shortage"]
    print(shortage[["Student_ID", "Name", "Attendance"]].to_string(index=False))

    # ---------------- Step 5: Save final output ----------------
    df.to_csv(OUTPUT_FILE, index=False)
    heading("ANALYSIS COMPLETE")
    print(f"Full results saved to: {os.path.basename(OUTPUT_FILE)}")


if __name__ == "__main__":
    main()
