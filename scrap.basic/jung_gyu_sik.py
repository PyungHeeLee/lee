import re
# 절차: 컴파일 (정규식 정의) -> 매치, 서치, 파인드올 (찾기) -> 그룹, 스트링, 스타트, 엔드, 스팬 (출력)
p = re.compile('ca.e')
    # . -> 하나의 문자 의미 (ca.e 등)
    # ^ -> 문자열의 시작 (^de 등)
    # $ -> 문자열의 끝 (se$ 등)

# match: 문자열의 처음 4글자와만 비교
m = p.match('case') # case 4글자가 ca.e에 match됨
m = p.match('my case') # 처음 4글자 'my c'가 match 안됨

# search: 모든 문자열 내에서 탐색 문자열이 있는지 확인
m = p.search('good case') # 문자열 안에 ca.e가 있으므로 search됨

# findall: 일치하는 모든것을 리스트 형태로 반환
m = p.findall('careless and my cafe') # care, cafe가 findall됨

def match(m):
    if m:
        print(m.group()) # 일치하는 문자열 반환
        print(m.string) # 입력받은 문자열 반환
        print(m.start()) # 일치하는 문자열의 시작 index (0:첫번째)
        print(m.end()) # 일치하는 문자열의 끝
        print(m.span()) # 일치하는 문자열의 시작/끝
    else:
        print('매칭 실패')

m = p.search('my cafe')
match(m)
'''
결과: my cafe의 처음 4글자는 ca.e에 match될 수 없으므로 매칭 실패
'''