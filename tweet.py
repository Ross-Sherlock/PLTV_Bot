import tweepy

CONSUMER_KEY = 'gaPGumV4F4R49IaUyTYnMolrw'
CONSUMER_SECRET = 'GWw7F3YID9Q13mnSVqI8XGkwdDepL7zghz0QHLApdCCsArFYWh'
ACCESS_KEY = '1488452318651629570-NeXZ0c9vPloP4Rwqx3DNTezXkoj5xJ'
ACCESS_SECRET = '3jbuXd53o36WT0fU6Q3cqeaVuhpHMYaOLOaxHlfLm78U5'

client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET)

client.create_tweet(text="hello")