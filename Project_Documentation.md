# Project Documentation

## 1. Project Title

**Student Performance Analytics System**

| | |
|---|---|
| Student | Atul *(add your full name)* |
| Program | B.Tech, Electronics and Communication Engineering (graduating 2027) |
| College | Truba Science and Technology College, Bhopal (RGPV) |
| Enrollment No. | *(add your enrollment number)* |
| Course | Python with AI, EWB Courses |

## 2. Objective

Teachers and institutions hold a lot of marks data, but raw numbers do not show who is performing well, which subjects are weak, or who is at risk. This project reads student records and automatically produces the answers: each student's total, average, grade and pass/fail result, the performance of every subject and department, the top performers, and students with low attendance. It replaces manual calculation with a repeatable Python program.

## 3. Technologies Used

- **Python 3**: variables, data types, conditions, loops and functions
- **NumPy**: numerical calculations on marks (sum, mean, median, standard deviation, min, max)
- **Pandas**: loading the CSV, DataFrame operations, filtering, sorting and groupby
- No other tools or libraries were used.

## 4. Dataset Description

`students.csv` contains **20 student records** and 9 columns:

| Column | Meaning |
|---|---|
| Student_ID | Unique ID, S001 to S020 |
| Name | Student name |
| Department | CSE, ECE, ME, CE, EE |
| Python, Mathematics, Physics, Electronics, English | Marks out of 100 |
| Attendance | Attendance percentage |

The data was created for this project. It includes a realistic spread: high scorers, average students, 3 students who fail a subject, and 5 students with attendance below 75%. There are no missing values.

## 5. Implementation

**Step 1: Load the data.** `load_data()` reads `students.csv` into a Pandas DataFrame. `main.py` prints the number of records, the column names, missing values and the first 5 rows.

**Step 2: Total and average.** `calculate_total_and_average()` converts the five subject columns into a 2D NumPy array and uses `np.sum(..., axis=1)` and `np.mean(..., axis=1)` to get each student's Total and Average in one operation.

**Step 3: Grade and result.** `add_grade_and_result()` loops over every student row.
- `get_result()` uses `np.all(marks >= 40)` so a student passes only if all subjects are at least 40.
- `assign_grade()` loops through the grade rule table (A+ for 90 and above, down to D for 40 and above, otherwise F).
- A student who fails any subject gets grade F.
- Attendance below 75% is marked "Shortage".

**Step 4: Analysis.** Separate functions answer each practical question:
- `class_statistics()`: class average, median, standard deviation, highest and lowest scorer
- `pass_fail_statistics()`: pass count, fail count, pass percentage
- `subject_analysis()`: loops through subjects and finds average, highest, lowest and pass % for each
- `top_performers()`: sorts by average and returns the top 5 with ranks
- `department_analysis()`: Pandas `groupby` for department-wise averages
- `grade_distribution()`: counts of students per grade

**Step 5: Final output.** `main.py` prints nine clearly headed sections and saves the complete table to `student_results.csv`.

## 6. Key Features

- Reads data from a CSV file using Pandas
- NumPy-based totals, averages and statistics
- Reusable functions kept in a separate `functions.py`
- Loops used for grading, subject analysis and result assignment
- Clearly defined grading rule and pass/fail condition
- Subject-wise, department-wise and grade-wise analysis
- Top 5 performers ranking
- Attendance shortage alert
- Results exported to `student_results.csv`

## 7. Output

Full console output is saved in `sample_output.txt`. Key results:

**Top 5 performers**

| Rank | Name | Department | Average | Grade |
|---|---|---|---|---|
| 1 | Muskan Khan | ECE | 91.6 | A+ |
| 2 | Anjali Mishra | CSE | 89.8 | A |
| 3 | Priya Verma | CSE | 89.2 | A |
| 4 | Divya Chouhan | CSE | 88.8 | A |
| 5 | Aarav Sharma | ECE | 83.0 | A |

**Subject-wise average**

| Subject | Average | Highest | Lowest | Pass % |
|---|---|---|---|---|
| English | 73.60 | 94 | 50 | 100 |
| Electronics | 69.85 | 95 | 41 | 100 |
| Python | 69.15 | 95 | 36 | 95 |
| Mathematics | 67.40 | 93 | 35 | 90 |
| Physics | 67.35 | 92 | 39 | 95 |

**Other results:** class average 69.47, 17 of 20 students passed (85%), average attendance 83.4%.

*(Optional: paste a screenshot of your terminal output here after running `python main.py`.)*

## 8. Final Outcome

The project runs without errors and answers every question in the assignment: the student with the highest average is Muskan Khan (91.6), the best subject is English (average 73.6), 17 of 20 students passed, and the overall class average is 69.47. The CSE department performs best (average 84.92) and the five students with attendance below 75% are listed. The output is readable without looking at the code. The results were cross-checked against a separate plain-Python calculation and matched.

## 9. Challenges and Learning

- **Grade for failed students.** A student with an average of 47 would get grade D, but failing a subject made that confusing. I fixed this by defining the rule that any subject below 40 means Fail and grade F.
- **Using NumPy and Pandas together.** I learned to pull marks out of a DataFrame with `to_numpy()`, do row-wise maths with `axis=1`, and put the results back as new columns.
- **Organising code.** Moving calculations into `functions.py` made `main.py` short and easy to read, and each function can be tested on its own.
- **Verifying results.** I learned to check program output with an independent calculation instead of trusting it blindly.

## 10. GitHub Repository

*(Paste your final repository link here, for example: https://github.com/your-username/student-performance-analytics)*
