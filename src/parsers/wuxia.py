import convert_to_file_name.convert_to_safe_file_name as convert
import os


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class Wuxia():
    def __init__(self,site,chapter_start,chapter_end):
        self.hdr = {'User-Agent': 'Mozilla/5.0'}
        self.site = site
        self.save_path = ''
        self.nextChapter = ''
        self.chapterStart = int(chapter_start)
        self.chapterEnd = int(chapter_end)

    def scrape(self):
        baseSite = "https://www.wuxiaworld.com"

        req = Request(self.site, headers=self.hdr)

        page = urlopen(req)
        soup = BeautifulSoup(page)
        folder = soup.find(class_='caption').find('h4')


        folder = convert.convert_to_file_name(str(folder.text))

        self.save_path = './'+str(folder)+'/'
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

        "Grabs a link to the next chapter"
        self.nextChapter = soup.find(class_='next').find(class_='btn btn-link').get('href')

        "Finds all the chapter content of the current chapter"
        results = soup.find('div', id='chapter-content').find_all("p")

        "Gets the current chapter header"
        chapter = soup.find('div', id='chapter-outer').find('h4')


        self.site = baseSite + self.nextChapter
        textfile = "Chapter " + str(self.chapterStart) + ".xhtml"
        completeName = os.path.join(self.save_path, textfile)


        f = open(completeName, "a", encoding='utf-8')
        f.write(str(chapter))



        for y in results:
            if results != None:
                f.write(str(y))
            else:
                return False

        self.site = baseSite + self.nextChapter

        f.close()
        self.chapterStart += 1
        return chapter



