import logging

from convert_to_safe_file_name import convert_to_file_name
import os


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def scrape(chapter,site):
    baseSite = "https://www.wuxiaworld.com"



    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)

    page = urlopen(req)
    soup = BeautifulSoup(page)
    folder = soup.find(class_='caption').find('h4')


    folder = convert_to_file_name(str(folder.text))

    save_path = './'+str(folder)+'/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    "Grabs a link to the next chapter"
    nextChapter = soup.find(class_='next').find(class_='btn btn-link').get('href')

    "Finds all the chapter content of the current chapter"
    results = soup.find('div', id='chapter-content').find_all("p")

    "Gets the current chapter header"
    chapter = soup.find('div', id='chapter-outer').find('h4')

    site = baseSite + nextChapter
    textfile = "Chapter " + str(chapter) + ".xhtml"
    completeName = os.path.join(save_path, textfile)

    f = open(completeName, "a", encoding='utf-8')
    f.write(str(chapter))

    site = baseSite + nextChapter

    f.close()

    return f

if __name__ == '__main__':
    scrape(1,'https://www.wuxiaworld.com/novel/second-life-ranker/slr-chapter-1')
