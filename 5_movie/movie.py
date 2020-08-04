import requests
from bs4 import BeautifulSoup
import csv 

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

soup1 = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li')

for j in soup1:
        a = j.select_one("dl > dt > a")

        movie_title = a.get_text()
        movie_link = a['href'].split("=")[-1]

        movie_list = [0,0]
        movie_list[0] = movie_title
        movie_list[1] = movie_link
        print(movie_list, '\n')

        with open('movie.csv', 'a', encoding = 'UTF-8-sig',newline='') as f:
            wr = csv.writer(f)
            wr.writerow(movie_list)


