from dotenv import load_dotenv
import tweepy
import os
from searchtweets import ResultStream, gen_request_parameters, load_credentials, collect_results
load_dotenv()
from datetime import datetime, timedelta, timezone
import yagmail

yag = yagmail.SMTP('nftynate@gmail.com', oauth2_file='~/oauth2_creds.json')
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAIWLaAEAAAAAxosFUwymx9RXMG9QxImF1O%2FhVxw%3D1dwv0vKAkS8BFSDcxdg293USBU63zJmWGOUl9DFb7Rb9b7NY1k", wait_on_rate_limit=True)

start_day = (datetime.now(timezone.utc) - timedelta(days=1))
words = ['Jazz', 'Utah', 'Clarkson']
total_tweets = []
all_members = []
members = client.get_list_members(id=887087, max_results=100) # Max for now; need to have
for member in members.data:
    member_id = member['id']
    all_members.append(member_id)

for member_id in all_members:
    tweets = client.get_users_tweets(id=member_id, start_time=start_day, exclude='retweets', max_results=5)
    try:
        for tweet in tweets.data:
            for word in words:
                if word in tweet.data['text']:
                    tweet_info = {}
                    tweet_info['username'] = (client.get_user(id=member_id)).data['username']
                    tweet_info['text'] = tweet.data['text']
                    tweet_info['tweet'] = ('https://twitter.com/twitter/statuses/' + tweet.data['id'])
                    total_tweets.append(tweet_info)
                    break
    except:
        continue

yag.send(to="nathaniel.hart@gmail.com", subject="Great!", contents=(f'Recent relevant tweets: {len(total_tweets)}', total_tweets))
