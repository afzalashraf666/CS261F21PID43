from bs4.element import Comment
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import re

genres = []
song_names = []
artist_names = []
release_dates = []
genre_tags = []
likes = []
reposts = []
plays = []
comments = []

driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver\chromedriver.exe')
'''
driver.get("https://www.chosic.com/list-of-music-genres/")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for instance in soup.findAll('li' , attrs={'class':'capital-letter genre-term'}):
    genre = instance.find('a', class_=False, id=False)
    genres.append(genre.text)
'''

url = "https://soundcloud.com/search/sounds?q=" + str("pop")
print("pop")
print("------")
driver.get(url)
time.sleep(1)

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 0

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for instance in soup.findAll('div' , attrs={'class':'sound__body'}):
    song_name = instance.find('span', class_='')
    artist_name = instance.find('div', class_='sc-type-light sc-text-secondary sc-text-h4 soundTitle__secondary')
    release_date = instance.find('div',  class_=['soundTitle__uploadTime sc-mb-0.5x', 'sc-visuallyhidden'])
    genre_tag = instance.find('span',  class_=['sc-truncate sc-tagContent'])
    like = instance.find('button',  class_= 'sc-button-like sc-button-secondary sc-button sc-button-small sc-button-responsive')
    repost = instance.find('button',  class_= 'sc-button-repost sc-button-secondary sc-button sc-button-small sc-button-responsive')
    
    play = instance.find('span',  class_=['sc-ministats sc-ministats-small sc-ministats-plays sc-text-secondary'])    
    play_child = play.find('span' , class_= 'sc-visuallyhidden')
    
    comment = instance.find('li',  class_=['sc-ministats-item'])
    temp = comment.find_next('li')
    print(temp.text)

    song_names.append(song_name.text)
    artist_names.append(artist_name.text.strip())

    release_date_int  = [int(s) for s in str(release_date).split() if s.isdigit()]
    release_date_int = 2021 - release_date_int
    release_dates.append(release_date_int)
    
    genre_tags.append(genre_tag.text)
    likes.append(like)
    reposts.append(repost)
    
    play_str = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', play_child.text)
    play_str = play_str[0].replace(',',"")
    plays.append(int(play_str))

    comments_str = ""
    for idx in range(19, len(temp.text)-1):
        print(temp.text[idx])
        comments_str+=temp.text[idx]
    comments.append(comments_str.strip())




    

print(comments)
dataset = [artist_names]
df = pd.DataFrame(data = dataset).T
df.columns = ["NAME"]
df.to_csv("datasets.csv" ,index=False)