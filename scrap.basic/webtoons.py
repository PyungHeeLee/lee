import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=783053'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 웹툰 전체 목록 가져오기
cartoons = soup.find_all('td', attrs={'class':'title'})

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com/' + cartoon.a['href']
    print(title, link)

for cartoon in cartoons:
    rank = cartoon.a.get_text() # 나중에 수정 바람
    link = 'https://comic.naver.com/' + cartoon.a['href']
    print(title, link)

cartoons = soup.find_all('div', attrs={'class':'rating_type'})
total = 0
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    total += float(rate) # int는 안됨
print('평균: {}'.format(total/len(cartoons)))

