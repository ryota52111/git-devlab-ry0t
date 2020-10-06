import csv
with open('passwd.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)

# print(csv.list_dialects())

# csv.register_dialect("hashes", delimiter="#", quoting=csv.QUOTE_NONE, lineterminator="\n")

# with open("items.csv", "r") as csvfile:
#     reader = csv.reader(csvfile, dialect="hashes")

#     for row in reader:
#         print(row)


# with open("items.csv", "a") as csvfile:
#     writer = csv.writer(csvfile, dialect="hashes")
#     writer.writerow(("spoon", 3, 1.5))
