import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv 


section ="정치"
url = "https://news.naver.com/main/main.nhn"
section_dict = { "정치" : 100,
                    "경제" : 101,
                    "사회" : 102,
                    "생활" : 103,
                    "세계" : 104,
                    "과학" : 105 }
req = requests.get(url, params={"sid1":section_dict[section]})
# <class 'bs4.BeautifulSoup'>
soup = BeautifulSoup(req.text, "html.parser")
a = soup.select("#today_main_news")
cnt = 0
for s in a:
    cnt +=1 
    print(cnt,"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;:",s)


print(cnt)