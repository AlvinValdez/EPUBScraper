import filecmp
import os
from src.parsers.wuxia import Wuxia



def test_scrape():

    test = Wuxia('https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-1',1,10)
    arrayOfHeaders = [
        '<h4 class="">Chapter 1 Memories of a Pill Sovereign</h4>',
        '<h4 class="">Chapter 2 Despicable Scum</h4>',
        '<h4 class="">Chapter 3 Revealing his Sharp Side</h4>',
        '<h4 class="">Chapter 4 Condensing the FengFu Star</h4>',
        '<h4 class="">Chapter 5 Imperial College </h4>',
        '<h4 class="">Chapter 6 Collecting Interest</h4>',
        '<h4 class="">Chapter 7 Training in Battle Skills</h4>',
        '<h4 class="">Chapter 8 Life and Death Battle</h4>',
        '<h4 class="">Chapter 9 Alchemist Guild</h4>'
    ]


    for x in range(test.chapterStart,test.chapterEnd):
        assert str(test.scrape()) == arrayOfHeaders[x-1]





    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 1.xhtml','testfiles/'+'test1.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 2.xhtml','testfiles/'+'test2.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 3.xhtml','testfiles/'+'test3.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 4.xhtml','testfiles/'+'test4.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 5.xhtml','testfiles/'+'test5.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 6.xhtml','testfiles/'+'test6.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 7.xhtml','testfiles/'+'test7.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 8.xhtml','testfiles/'+'test8.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 9.xhtml','testfiles/'+'test9.xhtml') == True


    os.remove('Nine-Star-Hegemon-Body-Art/'+'Chapter 1.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 2.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 3.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 4.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 5.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 6.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 7.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 8.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 9.xhtml')

