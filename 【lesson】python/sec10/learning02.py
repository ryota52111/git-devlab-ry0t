# import csv

# filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\csv_sample.csv"

# #Write
# with open(filename, "w", encoding="utf-8") as f:
#     writer = csv.writer(f, delimiter="*")

#     writer.writerow([1, 2, 3])
#     writer.writerow(["A", "B", "C"])

#     writer.writerows([[4,5,6,], ["D", "E", "F"]])

# import csv
# filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\csv_sample.csv"
# with open(filename, "w", encoding="utf-8", newline="") as f:
#     writer = csv.DictWriter(f, delimiter=",", fieldnames=["first_name","last_name"])

#     writer.writeheader()
#     writer.writerow({"first_name":"Tatsuya","last_name":"Nakamori"})
#     writer.writerow({"last_name":"Yamada","first_name":"Taro"})


import csv

filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\csv_sample.csv"

with open(filename, "r", encoding="utf-8") as f:
    # contents = f.read()

    # contents = f.readlines()

    # for row in f:
    #     print(row, end="")

    # reader = csv.reader(f, delimiter=",")
    # for row in reader:
    #     print(row)

    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        print(row["first_name"], row["last_name"])

