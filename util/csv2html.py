import csv
import sys

#watch out, chatgpt script

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} input.csv", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 3:
            continue  # skip malformed rows
        col1, col2, col3, col4 = row[0], row[1], row[2], row[3]
        print(f"<li><strong>{col1} {col2}</strong>, {col4}</li>")