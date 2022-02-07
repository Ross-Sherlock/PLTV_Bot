from selenium.common.exceptions import TimeoutException
import tweepy
from datetime import date
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True

url = "https://www.premierleague.com/broadcast-schedules"
s = Service('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=s)
driver.get(url)

try:
    # Wait until element located to prevent errors when finding unloaded elements
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "teams")))
    matchList = driver.find_element(By.CLASS_NAME, "matchList")
    team_elements = matchList.find_elements(By.CLASS_NAME, "teamName")
    broadcast_elements = matchList.find_elements(By.CLASS_NAME, "broadcaster-text")
    time_elements = matchList.find_elements(By.XPATH, '//time[not(@class)]')
    date_element = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div[2]/div[2]/time[1]/strong')
    upcoming_date = date_element.get_attribute('innerHTML')

    team_list = []
    broadcast_list = []
    time_list = []
    date_list = []

    for elem in time_elements:
        time_list.append(elem.get_attribute('innerHTML'))
    for elem in broadcast_elements:
        ## split at hyphen to return channel, return last element from resulting list
        ## as broadcaster
        element = elem.get_attribute('innerHTML').split("- ")[-1]
        broadcast_list.append(element)

    for elem in team_elements:
        team_list.append(elem.get_attribute('innerHTML'))

    total_teams = len(team_list)
    # Remove day sub-string from date string
    date_chars = []
    num_check = False
    for char in upcoming_date:
        if char.isdigit():
            num_check = True
        if num_check:
            date_chars.append(char)
    upcoming_date = "".join(date_chars, )

    # Convert date string into date object
    date_obj = datetime.datetime.strptime(upcoming_date, '%d %B %Y').date()
    today = date.today()

    # Get day difference between today and upcoming match
    delta_days = (date_obj - today).days
    print(delta_days)

    if delta_days == 1:
        ## add date just once as headline
        tweet_str = f"{upcoming_date}"
        for i in range(0, total_teams, 2):
            tweet_str += f"\n{time_list[i // 2]} {team_list[i]} vs {team_list[i + 1]} ({broadcast_list[i // 2]})"

        with open('prembotkeys.txt','r') as f:
            keys=[]
            for line in f:
                line = line.split(": ")
                keys.append(line[-1].rstrip())

        CONSUMER_KEY = keys[0]
        CONSUMER_SECRET = keys[1]
        ACCESS_KEY = keys[2]
        ACCESS_SECRET = keys[3]

        client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_KEY,access_token_secret=ACCESS_SECRET)

        client.create_tweet(text=tweet_str)

except TimeoutException:
    print("Timed out")


