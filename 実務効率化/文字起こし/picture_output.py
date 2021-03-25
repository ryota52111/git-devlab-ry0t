import glob
import os
from PIL import Image
import pyocr

#インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
#OS自体に設定してあれば以下の2行は不要
path='C:\\Program Files\\Tesseract-OCR'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]

 
save_name1 = []
book_name = "./result.xlsx"

files = glob.glob("./画像/*") #tmp内のファイルを取得
for file in files: #取得したファイルをforで回す。
    fail = os.path.basename(file)
    save_name1.append(fail) #tmp内のファイルをtextに格納

def read_file():
    for i, v in enumerate(save_name1):  
        img = Image.open(f"./画像/{v}")   #OCR対象の画像ファイルを読み込む
        builder = pyocr.builders.TextBuilder(tesseract_layout=6) #画像から文字を読み込む
        text = tool.image_to_string(img, lang="jpn", builder=builder)
        f = open(f'./結果/{v}.txt', 'w')
        f.write(text)
        f.close()

read_file()


 


 
