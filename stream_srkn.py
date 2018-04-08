from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import codecs
import json

access_token = "YOUR ACCESS_TOKEN"
access_token_secret = "YOUR ACCESS_TOKEN"
consumer_key = "YOUR CONSUMER_KEY"
consumer_secret = "YOUR CONSUMER_SECRET"


class StdOutListener(StreamListener):

    def on_data(self, raw_data):
        data = json.loads(raw_data)
        print(json.dumps(data, ensure_ascii=False))

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(languages=["tr"], track=["word1", "word2", "word3", "word4", "word5", "more..."])
	
