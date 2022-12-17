import snscrape.modules.twitter as sntwitter
import pandas as pd

query ='(from:ethiotelecom) until:2022-12-30 since:2010-01-01'
tweets = []
limit = 5000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)
df.to_csv('ethiotelecom_tweets.csv')