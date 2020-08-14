import openpyxl　#openpyxlインポート
import pandas as pd　#pandasインポート
import glob　#globインポート
import_file_path = '読み込みパス'　#windwosの場合は\\でパス表示
excel_sheet_name = '操作するシート名'
export_file_path = '出力先のパス'
df_order = pd.read_excel(import_file_path, sheet_name = excel_sheet_name)　#Excelのシートを読み込む
company_name = df_order['会社名'].unique()　#会社名という列の重複している行を消去する
for i in company_name:　#company_nameを順番に格納
        df_order_company = df_order[df_order['会社名'] == i]　#表示形式を変えてdf_order_companyへ代入
        df_order_company.to_excel(export_file_path+'/'+i+'.xlsx')　#iに格納したファイルをexport_file_pathへ出力