import requests
from bs4 import BeautifulSoup

nextURL = ""
URL = 'https://www.wuxia.blog/novel/A-Returners-Magic-Should-Be-Special/705291/Chapter-Epilogue-2.html'
fchp = 1
lchp = 315
for x in range(fchp,lchp):

    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    results = soup.find(class_='panel-body article')
    """nextURL = soup.find(class_='next').contents[0]['href']"""
    print(URL)

    URL = 'https://www.wuxia.blog'+nextURL



    if results != None:
        f = open(",Chapter "+str(x)+".xhtml","x",encoding='utf-8')
        f.write(str(results))
        f.close()
    else:
        x = x-1



