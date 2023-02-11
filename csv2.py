import csv


with open('price.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    with open('stage3_test.csv', 'r', encoding='utf-8') as d:
        reader = csv.reader(d)
        for row in reader:
            if row[4] == 'Price':
                pass
            elif 10000 < float(row[4]) <= 50000:
                writer.writerow(row)
