import csv

with open("students.csv") as f:
    students = [{k: int(v) for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]

print(",".join([student for student in students if student["year"] == 2023 and student["email"]]))
