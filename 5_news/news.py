import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv 

news_result = []

for i in range(1,102,10):
        
    st_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
    num_url = str(i)
    en_url = '&refresh_start=0'

    URL = st_url + num_url + en_url

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_result.append(soup)
print(type(soup))
print(len(news_result))
m = 0
for i in news_result:
        
    soup1 = i.select('ul[class=type01] > li')
    for j in soup1:
        a = j.select_one("dl > dt > a")

        news_title = a['title']
        news_link = a['href']
        m += 1
        print(m,news_title, news_link, '\n')

        news_list = [0,0]
        news_list[0] = news_title
        news_list[1] = news_link

        with open('news.csv', 'a', encoding = 'UTF-8-sig',newline='') as f:
            wr = csv.writer(f)
            wr.writerow(news_list)




