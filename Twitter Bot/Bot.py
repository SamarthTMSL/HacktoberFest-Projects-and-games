import tweepy

auth = tweepy.OAuthHandler("YOU_CONSUMER_KEY", "YOUR_CONSUMER_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_SECRET")
api = tweepy.API(auth)

#I will be changing my authorisation keys after demonstration, so I got that part covered.
# Tweet something
tweetstring = input("Enter the tweet: ")
tweet = api.update_status(tweetstring)
api.create_favorite(tweet.id)

FILE_NAME='last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read=open(FILE_NAME, 'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write=open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply ():
 
 hastag = input("Enter the hashtags to which you want to reply to: ")
 adireply=input("Enter the reply to the hashtags: ")
 tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
 for tweet in reversed(tweets):
        if (hastag) in tweet.full_text.lower():
            api.retweet(tweet.id)
            print("Heyyyy: " + str(tweet.id) + " - " + (adireply) + tweet.full_text.lower())
            tweet = api.update_status("@"+tweet.user.screen_name + adireply , tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
            quit()
while True:
    reply ()
    exit()
