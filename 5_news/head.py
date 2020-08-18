import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

result = []
k = soup.select("div[id=wrap]> div[id=container] > div[id=NM_INT_LEFT] > div[id=newsstand] > div[id=NM_NEWSSTAND_HEADER] > div[class=issue_area] > div[id=yna_rolling] > div")
for i in k:
    a_tag = i.select_one("a")
    for p in a_tag:
        print(p)
