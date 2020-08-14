from bs4 import BeautifulSoup　
import urllib.request as req
import pandas as pd　
url = "******" 	# urlにスクレイピングしたいURLを******に代入する
response = req.urlopen(url)　		#ダウンロード
parse_html = BeautifulSoup(response,'html.parser')	#URLのHTMLを解析
title_lists=parse_html.find_all('a')　#URLのすべてのaタグを解析
title_list=[]	#リストを定義
url_list=[]	#リストを定義
for i in title_lists:	#title_listsをiに繰り返し格納
        title_list.append(i.string)	#title_listに格納
        url_list.append(i.attrs['href'])	#hrefの要素のURLを格納
        title_list	#表示の確認
        url_list	#表示の確認
df_title_url = pd.DataFrame({'Title':title_list,'URL':url_list})	#データフレームの作成
df_title_url	#データフレームの確認
df_notnull = df_title_url.dropna(how='any')	#NoneやNullなどの欠損値を除く
df_notnull	#表示の確認
df_notnull['Title'].str.contains('*****')	#str.containsは特定の文字列を含むときはTure,含まないときはFalseをかえす。*****は特定の文字列を表す
df_notnull[df_notnull['Title'].str.contains('*****')]	#df_notnull['Title'].str.contains('*****')の結果を渡すとTrueだけが返ってくる
df_contain_python = df_notnull[df_notnull['Title'].str.contains('*****')]　#変数に代入
df_contain_python	#表示の確認
df_contain_python.to_csv(r"csvに代入したいファイルパス",encoding='utf-8-sig')	#ファイルパスを出力。,encoding='utf-8-sig'を追加すると文字コードをutf-8-sig形式にできる