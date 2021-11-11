import sys
import pytest
sys.path.insert(1, '../.')
from wuxia import scrape

def test_scrape():
    assert scrape(5,'https://www.wuxiaworld.com/novel/second-life-ranker/slr-chapter-1') == 'A-Record-of-a-Mortal’s-Journey-to-Immortality'
