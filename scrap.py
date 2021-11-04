from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
import time
import re

import Utilities
import FileSys

genres = []
song_names = []
artist_names = []
release_dates = []
genre_tags = []
likes = []
reposts = []
plays = []
comments = []

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver\chromedriver.exe' , options = options)

def get_genres():
    
    driver.get("https://www.chosic.com/list-of-music-genres/")
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    
    for instance in soup.findAll('li' , attrs={'class':'capital-letter genre-term'}):
        genre = instance.find('a', class_=False, id=False)
        genres.append(genre.text)

def get_songs():
    for idx in range(0,len(genres)):
    
        url = "https://soundcloud.com/search/sounds?q=" + str(genres[idx])
        driver.get(url)
        
        print("Genre Index:" ,idx)

        #for infinite down scrolling
        time.sleep(1)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 1000
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            print("Scroll:" , no_of_pagedowns)
            no_of_pagedowns-=1
        
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        
        for instance in soup.findAll('div' , attrs={'class':'sound__body'}):

            #finding attributes using classes
            song_name = instance.find('span', class_='')
            artist_name = instance.find('div', class_='sc-type-light sc-text-secondary sc-text-h4 soundTitle__secondary')
            release_date = instance.find('div',  class_=['soundTitle__uploadTime sc-mb-0.5x', 'sc-visuallyhidden'])
            genre_tag = instance.find('span',  class_=['sc-truncate sc-tagContent'])
            like = instance.find('button',  class_= 'sc-button-like sc-button-secondary sc-button sc-button-small sc-button-responsive')
            repost = instance.find('button',  class_= 'sc-button-repost sc-button-secondary sc-button sc-button-small sc-button-responsive')
            
            play = instance.find('span',  class_=['sc-ministats sc-ministats-small sc-ministats-plays sc-text-secondary'])

            if play is None:
                play_child = "0"
            else:
                play_child = play.find('span' , class_= 'sc-visuallyhidden')
                play_child = str(play_child.text)
            
            comment = instance.find('li',  class_=['sc-ministats-item'])

            if comment is None:
                temp = "0"
            else:
                temp = comment.find_next('li')
                temp = str(temp.text)
            

            #formatting and appending in lists
            song_namenillnot = Utilities.nonetyper(song_name)
            song_names.append(song_namenillnot.strip())

            artist_namenillnot = Utilities.nonetyper(artist_name)
            artist_names.append(artist_namenillnot.strip())

            release_date_int  = [int(s) for s in str(release_date).split() if s.isdigit()]
            release_date_int = 2021 - int(release_date_int[1])
            release_dates.append(release_date_int)
            
            genre_tagnillnot = Utilities.nonetyper(genre_tag)
            genre_tags.append(genre_tagnillnot.strip())
            
            likenillnot = Utilities.nonetyper(like)
            likenillnot = Utilities.garbage_remover(likenillnot)
            likes.append(likenillnot.strip())

            repostnillnot = Utilities.nonetyper(repost)
            repostnillnot = (repostnillnot).replace(',',"")
            repostnillnot = Utilities.garbage_remover(repostnillnot)
            reposts.append(repostnillnot.strip())
            
            play_str = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', play_child)
            play_strnillnot = Utilities.nonetyper(play_str[0])
            play_str = (play_strnillnot).replace(',',"")
            plays.append(play_str.strip())

            comments_str = ""
            for idx in range(19, len(temp)-1):
                comments_str+=temp[idx]
            comments_str = comments_str.strip()
            comment_strnillnot = Utilities.nonetyper(comments_str)
            comments_str = (comment_strnillnot).replace(',',"")
            
            #comments_str = Utilities.garbage_remover(comments_str)
            comments.append(comments_str.strip())
            print("Num:" ,len(comments))
            FileSys.store_csv(song_names, artist_names, plays, likes, comments, release_dates, reposts, genre_tags)