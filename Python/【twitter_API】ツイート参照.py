from requests_oauthlib import OAuth1Session
import json
CONSUMER_KEY = "" #Consumer Key (API key)
CONSUMER_SECRET = "" #Consumer Secret (API secret key)
ACCESS_TOKEN = "" #access_token
ACCESS_TOKEN_SECRET = "" #ACCESS_TOKEN_SECRET
twitter_api = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

def get_tweet(n):
  url = "https://api.twitter.com/1.1/statuses/user_timeline.json"　#statuses確認用
  params = {'count':100}
  result = twitter_api.get(url,params= params) 
  result = json.loads(result.text)
  print(result[n]['text'])

get_tweet(0) #何番目の投稿を取得するか。0は最新の投稿