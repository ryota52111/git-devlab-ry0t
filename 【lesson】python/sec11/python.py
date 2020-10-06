# import os
# print(os.path.abspath('foo.txt'))

# import os
# s = os.path.abspath(os.curdir) # os.curdir = '.'
# print(s)

# os.chdir(os.pardir) # os.pardir = '..'
# s = os.path.abspath(os.curdir)
# print(s)

# import sys
 
# sys.version

# import sys

# #↓ここでコマンドライン引数をargsという変数に格納
# args = sys.argv

# if len(args) == 3 :
#     print(args) #コマンドライン引数を出力
#     print(type(args)) #コマンドライン引数のデータ型を出力
#     print(type(args[2])) #コマンドライン第一引数のデータ型
#     print(len(args))
#     print("-"*30) #区切ってるだけ。意味はないです。

#     print("コマンドライン引数の第一引数は " + args[1] )
#     print(float(args[2])*3.14) #floatの意味は下に書きます。

# else:
#     print("コマンドライン引数を２つ入力してください \n 第一引数はstr型、第二引数はfloat型です。")

# import sys

# for i in range(100):
#   print(i)
#   if i == 10:
#     sys.exit()

# import os
# currnet_dir = os.path.dirname( os.path.abspath(__file__) )

# import os

# os.path.dirname(__file__)

# from pathlib import Path

# Path().resolve()