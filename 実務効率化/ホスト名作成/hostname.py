from openpyxl import load_workbook

excel_path = '#パス#\\サンプル.xlsx'

workbook = load_workbook(filename=excel_path, read_only=True)
sheet = workbook['採番']

B1 = sheet['B1'].value
B2 = sheet['B2'].value

for i in range(1,int(B2)):
    file_path = '#パス#ホスト名作成\\' + str(B1) + str(i) + '.txt'
    print(file_path)
    with open(file_path, 'w') as f:
        f.write('')
