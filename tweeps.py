from dotenv import load_dotenv
import tweepy
import slack
import os
import json
import time
from searchtweets import ResultStream, gen_request_parameters, load_credentials, collect_results
load_dotenv()
from datetime import datetime, timedelta, timezone, date
import yagmail

email_address_1 = 'jared@nftyarcade.io'
email_address_2 = 'talmage@nftyarcade.io'
slack_token = os.getenv('SLACK_OAUTH_TOKEN')
twitter_token = os.getenv('TWEEPY_BEARER_TOKEN')
twitter_list = 1503751904026890257
channel_name = "nfty-nate"
slack_client = slack.WebClient(token=slack_token)
yag = yagmail.SMTP('nftynate@gmail.com', oauth2_file='~/oauth2_creds.json')

def defaultconverter(o):
  if isinstance(o, datetime):
      return o.__str__()

client = tweepy.Client(twitter_token, wait_on_rate_limit=False)

start_day = (datetime.now(timezone.utc) - timedelta(days=1))
words = ['Event', 'Sale', 'Giveaway', 'Whitelist', 'Drop', 'Upcoming', 'Release', 'Mint']
total_tweets = []
all_members = []
members = client.get_list_members(id=twitter_list, max_results=100) # Max for now; need to have
for member in members.data:
    member_id = member['id']
    all_members.append(member_id)

for member_id in all_members:
    tweets = client.get_users_tweets(id=member_id, start_time=start_day, exclude='retweets', max_results=5, tweet_fields=['public_metrics','created_at'])
    try:
        for tweet in tweets.data:
            for word in words:
                if word in tweet['text']:
                    tweet_info = {}
                    # tweet_info['text'] = tweet['text']
                    # tweet_info['time_stamp'] = datetime.fromisoformat((tweet['created_at']).isoformat())
                    tweet_info['metrics'] = tweet['public_metrics']
                    tweet_info['tweet'] = ('https://twitter.com/twitter/statuses/' + str(tweet['id']))
                    total_tweets.append(tweet_info)
                    break
    except:
        continue
print("Total Tweets:", len(total_tweets))

# Posts a message for each tweet that applies.
for tweet in total_tweets:
    slack_client.chat_postMessage(channel=channel_name, text=json.dumps(tweet, default=defaultconverter, indent=2))
    time.sleep(10)
#
# # Get conversation_id, then ts/id's for messages, deletes messsages for THIS bot user (not previous ones)
# conversation_id = None
# for result in slack_client.conversations_list():
#     if conversation_id is not None:
#         break
#     for channel in result["channels"]:
#         if channel["name"] == channel_name:
#             conversation_id = channel["id"]
#             print(f"Found conversation ID: {conversation_id}")
#             break
#
# conversation_history = []
# result = slack_client.conversations_history(channel=conversation_id)
# conversation_history = result["messages"]
# for conversation in conversation_history:
#     message_id = conversation["ts"]
#     try:
#         slack_client.chat_delete(channel=conversation_id, ts=ts)
#         print(f"ts: {ts} was deleted.")
#     except:
#         print("Not the owner of this message.")

# yag.send(to=[email_address_1, email_address_2], subject=f'NFTy Nate Tweets as of {date.today()}', contents=(f'Recent relevant tweets: {len(total_tweets)}', total_tweets))

# Return the time and date that the tweet was sent.
# Return total number of likes, retweets, replies, quotes
# If a tweet passes a certain threshold while still being compliant with search parameters, send special email
# Slack integration?
