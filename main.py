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

## accept cookies popup
wait = WebDriverWait(driver, 1)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-accept-all-close")))
element.click()

## view full schedule
wait = WebDriverWait(driver, 1)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "broadcastFullSeasonButton")))
element.click()

"""A method for scrolling to the end of page"""

# Get scroll height.
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load the page.
    sleep(2)
    # Calculate new scroll height and compare with last scroll height.
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#sleep(5)
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

