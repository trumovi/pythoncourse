import csv


with open('image.csv', 'w', encoding='utf-8') as f:
    fieldnames = ["Id", "Images", "Title", "Description", "Price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    with open('stage3_test.csv', 'r', encoding='utf-8') as d:
        reader = csv.DictReader(d, delimiter=',')
        for row in reader:
            if len(row['Images'].split(',')) > 3:
                writer.writerow(row)
