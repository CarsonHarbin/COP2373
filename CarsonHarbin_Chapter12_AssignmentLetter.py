'''
Carson Harbin
Programming Exercise 12
This Program prompts the user to input the names of students, asks for three test scores for each,
and then calculates the mean, median, standard deviation, minimum, and maximum of the test scores.
'''

import csv
import numpy as np

def write_grades():
    filename = "grades.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))
            writer.writerow([first_name, last_name, exam1, exam2, exam3])
    print(f"Data successfully written to {filename}")

def analyze_grades():
    filename = "grades.csv"
    data = []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        #Skip header
        header = next(reader)
        for row in reader:
            #Only extract exam scores
            scores = list(map(int, row[2:]))
            data.append(scores)

    grades = np.array(data)
    print("\nFirst few rows of grade data:")
    print(grades[:5])

    print("\n--- Statistics per Exam ---")
    for i in range(grades.shape[1]):
        print(f"Exam {i+1}:")
        print(f"  Mean: {np.mean(grades[:, i]):.2f}")
        print(f"  Median: {np.median(grades[:, i]):.2f}")
        print(f"  Std Dev: {np.std(grades[:, i]):.2f}")
        print(f"  Min: {np.min(grades[:, i])}")
        print(f"  Max: {np.max(grades[:, i])}")

    print("\n--- Overall Statistics (All Exams Combined) ---")
    all_scores = grades.flatten()
    print(f"Mean: {np.mean(all_scores):.2f}")
    print(f"Median: {np.median(all_scores):.2f}")
    print(f"Std Dev: {np.std(all_scores):.2f}")
    print(f"Min: {np.min(all_scores)}")
    print(f"Max: {np.max(all_scores)}")

    print("\n--- Pass/Fail Stats Per Exam (Passing >= 60) ---")
    for i in range(grades.shape[1]):
        passed = np.sum(grades[:, i] >= 60)
        failed = np.sum(grades[:, i] < 60)
        print(f"Exam {i+1}: {passed} passed, {failed} failed")

    print("\n--- Overall Pass Percentage (All Exams) ---")
    total = grades.size
    passed_total = np.sum(grades >= 60)
    pass_percentage = (passed_total / total) * 100
    print(f"{passed_total} out of {total} grades are passing")
    print(f"Pass percentage: {pass_percentage:.2f}%")

write_grades()
analyze_grades()