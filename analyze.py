import csv

with open("students.csv") as f:
    students = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]

emails = [student["email"] for student in students if int(student["year"]) == 2023 and student["email"]]
print(",".join(emails))
