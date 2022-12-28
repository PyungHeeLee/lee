import requests
res1 = requests.get('https://nadocoding.tistory.com/')
res2 = requests.get('http://google.com')
print('응답:', res2.status_code) # 200이어야 정상

if res2.status_code == requests.codes.ok: # ok: 200
    print('정상')
else:
    print('비정상, 에러코드:', res2.status_code)

res2.raise_for_status() # 200이어야 함 -> 보통 위 requests get 문장과 함께 씀
print('웹 스크래핑 시작')
print(len(res2.text))
# print(res2.text)

with open('mygoogle.html', 'w', encoding='utf8') as f: # w: 덮어쓰기 모드
    f.write(res2.text)