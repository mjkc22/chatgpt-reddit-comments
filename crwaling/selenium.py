!pip install selenium==4.1.5
!pip install webdriver_manager
import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service #chromedriver 자동설치
from webdriver_manager.chrome import ChromeDriverManager #chromedriver 자동설치
from selenium.webdriver.common.by import By #요소 찾을 때 사용
service = Service(executable_path=ChromeDriverManager().install()) #크롬드라이버 설치
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get('http://naver.com')

# 요소를 찾기
first_sel = driver.find_element(By.ID, 'query')

# 데이터 입력하기
first_sel.send_keys('애플') 

# 요소를 클릭하기(검색버튼)
second_sel = driver.find_element(By.CLASS_NAME, 'ico_search_submit')
second_sel.click()

# 요소의 데이터를 가져오기(문자)
third_sel = driver.find_element(By.CLASS_NAME, 'news_tit')
third_sel.text

# 요소의 데이터를 가져오기(HTML)
third_sel = driver.find_element(By.CLASS_NAME, 'news_tit')
print(third_sel.get_attribute('innerHTML'))

import time

keywords = ['유아인','손흥민']
for i in keywords:
    time.sleep(1)
    # 사이트 접속
    driver.get('http://naver.com')
    # 요소를 찾기
    first_sel = driver.find_element(By.ID, 'query')
    # 데이터 입력하기
    first_sel.send_keys(i)
    # 요소를 클릭하기(검색버튼)
    second_sel = driver.find_element(By.CLASS_NAME, 'ico_search_submit')
    second_sel.click()
    # 요소의 데이터를 가져오기(문자)
    third_sel = driver.find_element(By.CLASS_NAME, 'news_tit')
    print(third_sel.text)
    # 요소의 데이터를 가져오기(HTML)
    third_sel = driver.find_element(By.CLASS_NAME, 'news_tit')
    print(third_sel.get_attribute('innerHTML'))
