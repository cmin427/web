import requests

headers = {
    'authority': 'search.shopping.naver.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&frm=NVSHATC&prevQuery=%EB%85%B8%ED%8A%B8%EB%B6%81',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=53H3YQNJI4AV6; MM_NEW=1; NFS=2; MM_NOW_COACH=1; NRTK=ag#30s_gr#1_ma#-2_si#0_en#0_sp#0; nx_ssl=2; ASID=76dbc2ac00000173a8fcb7ec0000005c; AD_SHP_BID=3; ncpa=1181635|kdo30t1k|71ebb45d1ff012127abf1ced9b5f987cbe8b1992|s_2633fcccceb5f|86ab107f32ed3b4fa8620938b594914e83c0948f:95694|kdo40rso|307fe49b2d59c46f8777d3ed7e85c00752e3e3f7|null|abb417671f957ae8069d22819e462e6eb473f3b1; JSESSIONID=D822C16516A81D38A22FE2E101BEF670; page_uid=UzvESlp0YidsscpLP2Nssssstzw-208212; spage_uid=UzvESlp0YidsscpLP2Nssssstzw-208212',
}

params = (
    ('query', '\uB178\uD2B8\uBD81'),
    ('frm', 'NVSHATC'),
    ('prevQuery', '\uB178\uD2B8\uBD81'),
)

response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&frm=NVSHATC&prevQuery=%EB%85%B8%ED%8A%B8%EB%B6%81', headers=headers)
