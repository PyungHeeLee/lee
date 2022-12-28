from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
options.add_argument(header)

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
browser.get(url)

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
browser.quit()