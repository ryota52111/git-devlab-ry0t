import glob
import os
import openpyxl

test = []
files = glob.glob("./tmp/*")
for file in files:
    split = os.path.split(file)[1]
    test.append(split)
print(test)

values = []
wb=openpyxl.load_workbook("ホスト名_チェック.xlsx")
sheet=wb["test1"]
for row in sheet.iter_rows(min_row=2):
        for col in row:
            values.append(col.value)
print(values)


l1_l2_and = set(test) ^ set(values)
with open('./差分.txt', 'w') as f:
    for ele in l1_l2_and:
      f.write(ele+'\n')