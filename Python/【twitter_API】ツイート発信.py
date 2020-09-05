from requests_oauthlib import OAuth1Session
import json
CONSUMER_KEY = "" #Consumer Key (API key)
CONSUMER_SECRET ="" #Consumer Secret (API secret key)
ACCESS_TOKEN = "" #access_token
ACCESS_TOKEN_SECRET = "" #ACCESS_TOKEN_SECRET
twitter_api = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

#ツイートする関数
def post_tweet():
  url = "https://api.twitter.com/1.1/statuses/update.json"
  tweet = input()#手入力
  params = {"status":tweet}
  twitter_api.post(url,params=params)
post_tweet()