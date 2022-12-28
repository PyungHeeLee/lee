import requests
url = 'https://nadocoding.tistory.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
# headers 정보는 what is my user? 사이트에서 가져옴
res = requests.get(url, headers=headers)
print(res.status_code) # 200이면 정상
res.raise_for_status()
print(len(res.text))
with open ('nadocoding.html', 'w', encoding='utf8') as f:
    f.write(res.text)
# nadocoding html은 복잡해서 브라우저로 여는데 오래 걸림