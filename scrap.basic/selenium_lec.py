# 터미널에서 작업할 것

# Python 입력으로 시작
from selenium import webdriver

browser = webdriver.Chrome() # 괄호 안에는 드라이버 위치 + 드라이버.exe
browser.get('https://www.naver.com/')
elem = browser.find_element_by_class_name('link_login')
elem.click()
browser.back()
browser.forward()
browser.refresh()
elem = browser.find_element_by_id('query')

from selenium.webdriver.common.keys import Keys
elem.send_keys('나도코딩')
elem.send_keys(Keys.ENTER)
elem = browser.find_elements_by_tag_name('a')
elem

for e in elem:
    elem.get_attribute('href')

browser.get('다음주소')
