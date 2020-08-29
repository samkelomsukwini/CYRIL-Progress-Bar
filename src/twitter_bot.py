import tweepy
import datetime

import config

consumer_key = config.CONSUMER_KEY
consumer_secret = config.CONSUMER_SECRET
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def bot():
    inaug = datetime.date(2019, 5, 25)
    today = datetime.date.today()
    diff = today - inaug
    
    numDiff = float(diff.days)
    yesterDiff = float(numDiff - 1) #will break on inaugeration day
    delta1 = numDiff / 1461
    delta2 = yesterDiff / 1461
    per1 = int(delta1 * 100)
    per2 = int(delta2 * 100)
    
    print("Yesterday: ")
    print(per2)
    print("Today: ")
    print(per1)

    numXs = per1 // 4
    numSpaces = 25 - numXs
    c = ("▓" * numXs) + ("░" * numSpaces)
    tweetString = "The president's term is " + str(per1) + "% complete\n" + c
    
    try:
        api.update_status(tweetString+'\n'+'\n'+'#cyril #ancmustfall #mashaba #southafrica')
    except tweepy.TweepError as e:
        print(e)

def main():
    bot()


if __name__ == "__main__":
    main()
