import csv
from collections import OrderedDict

with open('stage3_test.csv', 'r', encoding='utf-8') as d:
    reader = csv.DictReader(d, delimiter=',')
    price = {}
    for row in reader:
        price[row['Title']] = float(row["Price"])

dict = OrderedDict(sorted(price.items(), key=lambda t: t[1]))
# print(dict)
dict1 = OrderedDict(sorted(price.items(), key=lambda t: t[1], reverse=True))
# print(dict1)

with open('price_from_lowest.csv', "w", encoding='utf-8') as g:
    writer = csv.writer(g)
    for item in dict:
        writer.writerow([item, dict[item]])
with open('price_from_highest.csv', 'w', encoding='utf-8') as w:
    writer = csv.writer(w)
    for item in dict1:
        writer.writerow([item, dict1[item]])