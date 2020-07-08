"""
Post a response to every mention on twitter.
"""
import tweepy
import time

def getLastTweetId(fileName):
    read = open(fileName, 'r')
    lastTweetId = int(read.read().strip())
    read.close()
    return lastTweetId

def saveLastTweetId(lastTweetId, fileName):
    write = open(fileName, 'w')
    write.write(str(lastTweetId))
    write.close()
    return

def replyToTweets(api, fileName = 'LastTweetId.txt'):
    #Test Id: YOUR_TEST_ID
    #Only get unseen tweets

    #mentions = api.mentions_timeline()
    #print(mentions[0].__dict__.keys())
    lastTweetId = getLastTweetId(fileName)
    mentions = api.mentions_timeline(lastTweetId, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        city = mention.full_text.lower()

        lastTweetId = mention.id 
        saveLastTweetId(lastTweetId, fileName)
        print(mention.id)

        if('@YOU_USER_NAME ' in city):
            city = city.replace('@YOU_USER_NAME ', '')
            city = city.replace(' ', ',')
            print('Respondiendo...')
            api.update_status('@{} Gracias por usar este Bot :D'.format(mention.user.screen_name), mention.id)
            
        elif ('@YOU_USER_NAME' in city):
            city = city.replace('@YOU_USER_NAME', '')
            city = city.replace(' ', ',')
            print('Respondiendo...')
            api.update_status('@{} Gracias por usar este Bot :D'.format(mention.user.screen_name), mention.id)

print('Twitter Bot')
CONSUMER_KEY = 'YOUR_API_KEY'
CONSUMER_SECRET = 'YOUR_API_SECRET'
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    replyToTweets(api)
    time.sleep(2)