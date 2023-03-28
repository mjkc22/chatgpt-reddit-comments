# 전화번호 수집 크롤링
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

l= []
for i in tqdm(range(194127,195617)):
    url = f"http://lessoninfo.co.kr/board/board.php?board_code=20130529164321_7227&code=20170307205423_8969&bo_table=20161206194557_6971&wr_no={i}"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    try :
        elements = soup.find(class_='telWrap').get_text()
    except :
        continue
    l.append(elements)
