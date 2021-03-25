import glob
import os
import openpyxl

values = []
wb=openpyxl.load_workbook("ホスト名_チェック.xlsx")
sheet=wb["test1"]
for row in sheet.iter_rows(min_row=2):
        for col in row:
            values.append(col.value)

for i in range(1,len(values) - 1):
    file_path = './tmp/' + str(values[i]) + '.txt'
    with open(file_path, 'w') as f:
        f.write(str(values[i]))

