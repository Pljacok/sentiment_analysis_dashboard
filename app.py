import tweepy
from textblob import TextBlob

auth = tweepy.OAuth1UserHandler("API_KEY", "API_SECRET", "ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

tweets = api.search_tweets("crypto", count=10)
for tweet in tweets:
    sentiment = TextBlob(tweet.text).sentiment.polarity
    print(f"Твіт: {tweet.text} | Настрій: {sentiment}")
