import requests
from bs4 import BeautifulSoup
import time
import random

def save_problems():
    page_url = "http://www7b.biglobe.ne.jp/~browneye/english/TOEIC400-1.htm"
    r = requests.get(page_url)
    r.encoding = r.apparent_encoding #本来取得するべき文字コードを取得する
    soup = BeautifulSoup(r.text, features= "html.parser")
    td_list = soup.find_all("td")
    print(td_list)
    td_values = [x.text for x in td_list]
    print(td_values)
    splited_list = []
    for index in range(0, len(td_values),4): #4つずつリストを別のリストに入れる
        a = td_values[index: index + 4] #スライスを使ってリストの塊を出す。
        
        if a[0] == '\u3000':
          continue #除外するcontinueを使うことでfor文のループを回すことができます。
        splited_list.append(a)
    
    print(splited_list)
    with open(r"C:\Users\r_sas\Desktop\words.txt", "w") as f:
        for value in splited_list:
            f.write("{},{}\n".format(value[1],value[2])) #format関数で出力する文字の順番を決める。

def get_problems():
    with open(r"C:\Users\r_sas\Desktop\words.txt","r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems] #改行コードを削除する
    
    return problems

def start_english_words_test(problems):
    for index, p in enumerate(problems): #enumerateを使ってインデックスを取得することができる
        x = p.split(",")
        english = x[0]
        japanese = x[1]
        print("====第{}問目====".format(index + 1)) #今何問目かを表示させます。
        print(english)
        time.sleep(2)
        print(japanese)
        time.sleep(0)

def main():
    p = get_problems()
    random.shuffle(p)
    start_english_words_test(problems=p)
        
        
        
main() 