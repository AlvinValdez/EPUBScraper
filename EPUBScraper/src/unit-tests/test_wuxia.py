import filecmp
import os
import sys
import pytest
sys.path.insert(1, '../.')
from wuxia import scrape

def test_scrape():
    assert str(scrape(1,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-1')) == '<h4 class="">Chapter 1 Memories of a Pill Sovereign</h4>'
    assert str(scrape(2,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-2')) == '<h4 class="">Chapter 2 Despicable Scum</h4>'
    assert str(scrape(3,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-3')) == '<h4 class="">Chapter 3 Revealing his Sharp Side</h4>'
    assert str(scrape(4,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-4')) == '<h4 class="">Chapter 4 Condensing the FengFu Star</h4>'
    assert str(scrape(5,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-5')) == '<h4 class="">Chapter 5 Imperial College </h4>'
    assert str(scrape(6,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-6')) == '<h4 class="">Chapter 6 Collecting Interest</h4>'
    assert str(scrape(7,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-7')) == '<h4 class="">Chapter 7 Training in Battle Skills</h4>'
    assert str(scrape(8,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-8')) == '<h4 class="">Chapter 8 Life and Death Battle</h4>'
    assert str(scrape(9,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-9')) == '<h4 class="">Chapter 9 Alchemist Guild</h4>'
    assert str(scrape(10,'https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-10')) == '<h4 class="">Chapter 10 Disciplining the Brat</h4>'




    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 1.xhtml','Nine-Star-Hegemon-Body-Art/'+'test1.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 2.xhtml','Nine-Star-Hegemon-Body-Art/'+'test2.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 3.xhtml','Nine-Star-Hegemon-Body-Art/'+'test3.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 4.xhtml','Nine-Star-Hegemon-Body-Art/'+'test4.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 5.xhtml','Nine-Star-Hegemon-Body-Art/'+'test5.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 6.xhtml','Nine-Star-Hegemon-Body-Art/'+'test6.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 7.xhtml','Nine-Star-Hegemon-Body-Art/'+'test7.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 8.xhtml','Nine-Star-Hegemon-Body-Art/'+'test8.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 9.xhtml','Nine-Star-Hegemon-Body-Art/'+'test9.xhtml') == True
    assert filecmp.cmp('Nine-Star-Hegemon-Body-Art/'+'Chapter 10.xhtml','Nine-Star-Hegemon-Body-Art/'+'test10.xhtml') == True

    os.remove('Nine-Star-Hegemon-Body-Art/'+'Chapter 1.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 2.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 3.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 4.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 5.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 6.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 7.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 8.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 9.xhtml')
    os.remove('Nine-Star-Hegemon-Body-Art/' + 'Chapter 10.xhtml')
