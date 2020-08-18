import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv 

url = "https://music.bugs.co.kr/chart"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

bugs = soup.select("div[id=wrap] > div[id=hyrendContentBody] > article[id=container] > section[class=sectionPadding] > ")
print(bugs)


