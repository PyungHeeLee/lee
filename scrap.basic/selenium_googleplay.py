from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://play.google.com/store/movies'
browser.get(url)

# browser.execute_script('window.scrollTo(0, -1080)') # -2080

# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

import time
interval = 2

prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script('return document.body.scrollHeight')
    time.sleep(interval)

    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break

    prev_height = curr_height

print('스크린 완료')

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs={'class':'Vpfmgd'})
print(len(movies))

for movie in movies:
    title = movie.find('div', attrs={'class':'WsMG1c nnK0zc'})
    orginal_price = movie.find('span', attrs={'class':'SUZt4c djCuy'})
    if orginal_price:
        orginal_price = orginal_price.get_text()
    else:
        continue

    price = movie.find('span', attrs={'class':'VfPpfd ZdBevf i5DZme'}).get_text()

    link = movie.find('a', attrs={'class':'3C71ub'})['href']

    print(f'제목: {title}')
    print(f'할인 전: {orginal_price}')
    print(f'할인 후: {price}')
    print('링크:', 'https://play.google.com'+link)
    print('-'*100)

browser.quit()