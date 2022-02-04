import tweepy
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True

url = "https://www.premierleague.com/broadcast-schedules"
s = Service('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=s)
driver.get(url)

sleep(5)
team_elements = driver.find_elements(By.CLASS_NAME, "teamName")
broadcast_elements = driver.find_elements(By.CLASS_NAME, "broadcaster-text")
team_list = []
broadcast_list = []

for elem in broadcast_elements:
    broadcast_list.append(elem.get_attribute('innerHTML'))

del broadcast_list[:3]

for elem in team_elements:
    team_list.append(elem.get_attribute('innerHTML'))

total_teams = len(team_list)
for i in range(0, total_teams, 2):
    print(team_list[i], "vs", team_list[i+1], "- On ", broadcast_list[i//2])

CONSUMER_KEY = 'gaPGumV4F4R49IaUyTYnMolrw'
CONSUMER_SECRET = 'GWw7F3YID9Q13mnSVqI8XGkwdDepL7zghz0QHLApdCCsArFYWh'
ACCESS_KEY = '1488452318651629570-NeXZ0c9vPloP4Rwqx3DNTezXkoj5xJ'
ACCESS_SECRET = '3jbuXd53o36WT0fU6Q3cqeaVuhpHMYaOLOaxHlfLm78U5'

client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET)

client.create_tweet(text="hello")


