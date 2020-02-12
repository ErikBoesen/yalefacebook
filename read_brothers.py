import csv

with open('brothers.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row[0])
