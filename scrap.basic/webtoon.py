# 터미널에서 pip install beautifulsoup4, pip install lxml
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 처음 발견되는 a element 반환
# print(soup.a.attrs) # a element 속성 (dict 형식)
# print(soup.a['href']) # a element 속성의 href 정보 반환

# print(soup.find('a', attrs={'class':'Nbtn_upload'})) # 웹툰올리기 찾기, 선행:태그(a, div 등), 후행 : 조건

rank1 = soup.find('li', attrs={'class':'rank01'}) # 급상승 1위 웹툰
# print(rank1.a)
# print(rank1.a.get_text)

# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text)

# rank2 = rank3.previous_sibling.previous_sibling

# print(rank1.parent) # 부모

# rank2 = rank1.find_next_sibling('li') # 조건(li)에 맞는 후행자 찾기
# print(rank2.a.get_text())

# rank2 = rank1.find_next_siblings('li') # 한꺼번에 여러 후행자

webtoon = soup.find('a', text='참교육-106화') # 특정 텍스트 찾기, 텍스트: 웹 검사에서 참고
print(webtoon)
