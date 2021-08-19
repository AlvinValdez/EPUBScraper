import requests
from bs4 import BeautifulSoup
"""
chp = 131
for x in range(1,131):
    URL = 'https://woopread.com/series/sss-class-suicide-hunter/chapter-'+str(x)+'/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    results = soup.find(class_='reading-content')

    print(results)

    if results != None:
        f = open("Chapter "+str(x)+".xhtml","x",encoding='utf-8')
        f.write(str(results))
        f.close()
    else:
        x = x-1
"""

URL = 'https://woopread.com/series/sss-class-suicide-hunter/chapter-109-1/'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')

results = soup.find(class_='reading-content')

print(results)

f = open("Chapter 109-1.xhtml","x",encoding='utf-8')
f.write(str(results))
f.close()