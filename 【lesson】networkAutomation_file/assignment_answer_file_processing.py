# with open("devices.txt") as f:
#     devices = f.read().splitlines()
#     print(devices)

# mylist = list()
# for item in devices:
#     tmp = item.split(":")
#     print(tmp)
#     mylist.append(tmp)

# print(mylist)

import csv
with open("devices.txt") as f:
    reader = csv.reader(f, delimiter=":")
    mylist = list()
    for row in reader:
        mylist.append(row)
    


    print(mylist)