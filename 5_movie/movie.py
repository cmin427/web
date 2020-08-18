import requests
from bs4 import BeautifulSoup
import csv 

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

soup1 = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li')

final_movie = []

for j in soup1:
        a = j.select_one("dl > dt > a")

        movie_title = a.get_text()
        movie_link = a['href'].split("=")[-1]

        movie_list = [0,0]
        movie_list[0] = movie_title
        movie_list[1] = movie_link
        final_movie.append(movie_list)
        with open('movie.csv', 'a', encoding = 'UTF-8-sig',newline='') as f:
            wr = csv.writer(f)
            wr.writerow(movie_list)

print(final_movie,len(final_movie))

reviews_url_f = "https://movie.naver.com/movie/bi/mi/basic.nhn?code="
reviews_url_b = "&page="

for i in final_movie:
    # i[0] title
    # i[1] code
    reviews_page = 0
    for page in range(10):
        reviews_page += 1   
        reviews_url = reviews_url_f + str(i[1]) + reviews_url_b + str(reviews_page)
        response = requests.get(reviews_url)
        review_soup = BeautifulSoup(response.text, 'html.parser')





import requests

headers = {
    'authority': 'movie.naver.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://movie.naver.com/movie/bi/mi/review.nhn?code=185917&page=1',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=53H3YQNJI4AV6; MM_NEW=1; NFS=2; MM_NOW_COACH=1; NRTK=ag#30s_gr#1_ma#-2_si#0_en#0_sp#0; nx_ssl=2; ASID=76dbc2ac00000173a8fcb7ec0000005c; NM_THUMB_PROMOTION_BLOCK=Y; csrf_token=4b7f5ce3-d4b1-4479-99ea-d0e3cdda0762',
}

params = (
    ('code', '185917'),
)

response = requests.get('https://movie.naver.com/movie/bi/mi/review.nhn', headers=headers, params=params)


