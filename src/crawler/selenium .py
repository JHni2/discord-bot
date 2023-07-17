from selenium import webdriver as wb
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

driver = wb.Chrome() 
keyword = '윤하'
url = f'https://www.youtube.com/results?search_query={keyword}'
driver.get(url)

body = driver.find_element(By.TAG_NAME,'body')
body.send_keys(Keys.PAGE_DOWN)

# for i in range(1,51):
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.5)

soup = bs(driver.page_source, 'lxml')

res = []

# 영상 썸네일
thumbnail = soup.select('#thumbnail > yt-image > img') 
for idx, val in enumerate(thumbnail[:10]):
   if 'src' in val.attrs:
    if idx >= len(res):
            res.append({
                'thumbnail': val.attrs['src'],
                'title': '',
                'href': '',
            })
    else:
        # 이미 존재하는 딕셔너리 업데이트
        res[idx].update({
            'thumbnail': val.attrs['src'],
        })
    
# 영상 제목, 링크 
title = soup.select('a#video-title')
for idx, val in enumerate(title[:10]):
  if idx >= len(res):
            res.append({
                'title': val.text.strip(),
                'href': 'https://www.youtube.com' + val.attrs['href'],
            })
  else:
      # 이미 존재하는 딕셔너리 업데이트
      res[idx].update({
          'title': val.text.strip(),
          'href': 'https://www.youtube.com' + val.attrs['href'],
      })

print(res)
