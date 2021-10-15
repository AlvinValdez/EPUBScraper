
import os

save_path = './chapters/'
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def scrape(fchap, lchap,site):
    baseSite = "https://www.wuxiaworld.com"


    for x in range(fchap, lchap):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)

        page = urlopen(req)
        soup = BeautifulSoup(page)
        nextChapter = soup.find(class_='next').find(class_='btn btn-link').get('href')
        results = soup.find('div', id='chapter-content').find_all("p")
        chapter = soup.find('div', id='chapter-outer').find('h4')
        site = baseSite + nextChapter
        textfile = "Chapter " + str(x) + ".xhtml"
        completeName = os.path.join(save_path, textfile)

        f = open(completeName, "a", encoding='utf-8')
        f.write(str(chapter))

        for y in results:
            if results != None:
                f.write(str(y))

            else:
                x = x - 1

        site = baseSite + nextChapter


        f.close()
