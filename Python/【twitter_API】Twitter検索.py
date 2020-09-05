from requests_oauthlib import OAuth1Session
import json
import pandas as pd
#取得ツイート集
count = 100
#検索ワード
search_word = '検索したいワード　-filter:retweets'

CK = "" #Consumer Key (API key)
CS = "" #Consumer Secret (API secret key)
AT = "" #access_token
AS = "" #ACCESS_TOKEN_SECRET

twitter_api = OAuth1Session(CK,CS,AT,AS)

#ツイートの検索・取得
url = "https://api.twitter.com/1.1/search/tweets.json"
params = {'q':search_word,'lang':'ja','count':count}
results = twitter_api.get(url,params=params)
results = json.loads(results.text)
data_raw = pd.DataFrame(results['statuses'])
data_raw

data_new  = data_raw[['created_at','user','text','favorite_count','retweet_count']]
data_new

#　ユーザー名を表示
for result in results['statuses']:
  print(result['user']['id'])

#ユーザidとユーザー名を別々に取得
user_id = []
user_name = []

for resuit in results['statuses']:
    user_id.append(result['user']['id'])
    user_name.append(result['user']['name'])

# data_newにユーザーidとユーザ名を追加
data_new.insert(2,'user_id',user_id)
data_new.insert(3,'user_name',user_name)
data_new

#いいねの多いい順番に並べ替え
data_sorted = data_new.sort_values("favorite_count", ascending = False)
data_sorted

data_sorted.to_csv(r'出力したいパス',encoding='utf_8_sig') #google Colaboratory