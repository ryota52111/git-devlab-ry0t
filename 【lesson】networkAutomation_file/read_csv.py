# import csv
# with open('airtravel.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     year_1958 = dict()
#     for row in reader:
#         year_1958[row[0]] = row[1]

#     print(year_1958)

#     max_1958 = max(year_1958.values())

#     print(max_1958)

#     for k, v in year_1958.items():
#         if max_1958 == v:
#             print(f"Busiest Month in 1958:{k}, Flight:{v.strip()}")

#-------------------------------------------------------------------------

import csv
# with open ('people.csv', 'a') as csvfile:
#     writer = csv.writer(csvfile)
#     csvdata = (5, 'Anne', 'Amsterdam')
#     writer.writerow(csvdata)

with open("numbers.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x", "x**2", "x**3", "x**4"])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])