from convert_to_file_name.convert_to_safe_file_name import convert_to_file_name
import os


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def pubscrape(fchap, lchap,site):
    """
    Takes a first chapter and last chapter along with what chapter to begin scraping from.(Site is a link to that chapter)
    :param fchap:
    :param lchap:
    :param site:
    :return:
    """
    baseSite = "https://www.lightnovelpub.com"


    """
    folder = soup.find(class_='booktitle').text
    print(folder)
    chapter = soup.find(class_='chapter-title')
    print(chapter)
    """


    for x in range(fchap, lchap):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)

        page = urlopen(req)
        soup = BeautifulSoup(page)
        folder = soup.find(class_='booktitle')


        folder = convert_to_file_name(str(folder.text))

        save_path = './'+str(folder)+'/'
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        "Grabs a link to the next chapter"
        nextChapter = soup.find(class_='nextchap').get('href')

        "Finds all the chapter content of the current chapter"
        results = soup.find('div', id='chapter-container').find_all("p")

        "Gets the current chapter header"
        chapter = soup.find(class_= 'chapter-title')
        chapter.name='h4'
        site = baseSite + nextChapter
        textfile = "Chapter " + str(x) + ".xhtml"
        completeName = os.path.join(save_path, textfile)

        f = open(completeName, "a", encoding='utf-8')
        f.write(str(chapter))

        for y in results:

            "Checks if the content was actually scraped successfully. If not it tries again"
            if results != None:
                f.write(str(y))

            else:
                x = x - 1

        site = baseSite + nextChapter


        f.close()


if __name__ == '__main__':
    pubscrape(1,10,"https://www.lightnovelpub.com/novel/tensei-shitara-slime-datta-ken-ln-19072354/chapter-0")