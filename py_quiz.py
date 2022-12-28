# 퀴즈1
# station = '사당'
# print(station + '행 열차가 들어오고 있습니다.')
# #print(station, '행 열차가 들어오고 있습니다.')

# 퀴즈2
# from random import *
# x = int(random() * 25) + 4
# print('오프라인 모임 날짜는 매월 ', x, '일로 정해졌습니다.')

# 퀴즈3
# a = 'http://naver.com'
# a = a.replace('http://', '')
# a = a[:a.index('.')]
# print(a)
# a = a[:3] + str(len(a)) + str(a.count('e')) + '!'
# print('제 pw는', a, '입니다.')

# 퀴즈4
# from random import *
# user = range(1,21)
# print(user, type(user))
# user = list(user)
# print(user, type(user))
# shuffle(user)
# print(user)
# winner = sample(user, 4)
# print(winner)
# print('당첨자 발표')
# print('치킨 당점자: {0}'.format(winner[0]))
# print('커피 당첨자: {0}'.format(winner[1:4]))

# 퀴즈5
'''from random import *
c=0
for i in range(1,51):
    t = randint(5,50)
    if 5 <= t <= 15:
        c+=1
        print('[o] {0}번째 손님 (소요시간: {1}분)'.format(i,t))
    else:
        print('[x] {0}번째 손님 (소요시간: {1}분)'.format(i,t))
print('총 탑승 승객: {0}'.format(c))'''

'''i=2
# 퀴즈6
def weight(sex, height):
    if sex == 'm':
        std_weight = round((height **2 *22 /10000), 2)
    else:
        std_weight = round((height **2 *21 /10000), 2)
    print('{} 키 {}의 표준 체중은 {}kg입니다.'.format(sex, height, std_weight))
    i=5
weight('w', 175)
print(i)'''

# 퀴즈7
'''from pickle import *
for i in range(1,11):
    with open('{}주차.txt'.format(i), 'w', encoding='utf8') as file:
        file.write('{}주차 보고서\n\n # 부서 :\n# 이름 :\n# 업무 요약: '.format(i))'''

# 퀴즈8  
'''class house:
        def __init__(self, loca, h_t, p_t, p, y):
            self.loca = loca
            self.h_t = h_t
            self.p_t = p_t
            self.p = p
            self.y = y
        def show(self):
            print('집 정보: {}지역 {}, {} {}, 준공 {}'.format(self.loca, self.h_t, self.p_t, self.p, self.y))
    
a1 = house('대구', '아파트', '월세', '500/50', 2019)
a1.show()'''

# 퀴즈9
'''class sold(Exception):
    def __init__(self, msg):
        self.msg = msg
chicken=10
wait=1
while True:
    try:
        n = int(input('치킨?'))
        if n<1 or n>chicken:
            raise ValueError
        if chicken < 1:
            raise sold('매진,,')
        else:
            chicken -= n
            wait += 1
            print('주문 완료, 치킨 {}마리 남음, 웨이팅 {}팀'.format(chicken, wait))
            if chicken == 0:
                raise sold('주문 완료! 그리고 매진,,,')
    except ValueError:
        print('잘못된 값, 1 이상 {} 이하로 주문 바람'.format(chicken))
    except sold as err:
        print(err)
        break'''

# 퀴즈10
'''class sign1():
    def sign2():
        print('this is nado coding2')

def sign3():
        print('this is nado coding3')'''
'''이 파일을 따로 만들어주면 된다
파일명.클래스명.함수명() 해주거나 파일명.함수명() 해서 접근 가능'''