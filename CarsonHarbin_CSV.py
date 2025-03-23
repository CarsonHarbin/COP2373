import csv

def write_grades():
    filename = "grades.csv"

    #Open file in write mode
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        #Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        #Get number of students
        num_students = int(input("Enter the number of students: "))

        for _ in range(num_students):
            #Get student details
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            #Write to CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"Data successfully written to {filename}")


def read_grades():
    filename = "grades.csv"

    #Open file in read mode
    with open(filename, mode="r") as file:
        reader = csv.reader(file)

        #Read and display data
        header = next(reader)
        print(f"{header[0]:<12} {header[1]:<12} {header[2]:<7} {header[3]:<7} {header[4]:<7}")
        print("-" * 45)

        for row in reader:
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<7} {row[3]:<7} {row[4]:<7}")