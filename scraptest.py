from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

genres = []

driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver\chromedriver.exe')
driver.get("https://www.chosic.com/list-of-music-genres/")
content = driver.page_source
soup = BeautifulSoup(content)

for instance in soup.findAll('li' , attrs={'class':'capital-letter genre-term'}):
    genre = instance.find('a', class_=False, id=False)
    genres.append(genre.text)

for Index in genres:
    print(Index)