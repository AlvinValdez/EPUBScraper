import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

baseSite="https://www.wuxiaworld.com"
site= "https://www.wuxiaworld.com/novel/the-regressed-demon-lord-is-kind/rdk-chapter-1"
fchap=1
lchap=100
for x in range(fchap,lchap):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)

    page = urlopen(req)
    soup = BeautifulSoup(page)
    nextChapter = soup.find(class_='next').find(class_='btn btn-link').get('href')
    results = soup.find('div', id='chapter-content').find_all("p")

    for y in results:
        if results != None:
            f = open("Chapter "+str(x)+".xhtml","a",encoding='utf-8')
            f.write(str(y))

        else:
            x = x-1


    site = baseSite + nextChapter

    print(site)
    f.close()
