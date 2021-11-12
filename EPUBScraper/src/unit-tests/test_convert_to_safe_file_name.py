import sys
from convert_to_file_name.convert_to_safe_file_name import convert_to_file_name

def test_convert_to_file_name():
    assert convert_to_file_name('A Record of a Mortal’s Journey to Immortality') == 'A-Record-of-a-Mortal’s-Journey-to-Immortality'
    assert convert_to_file_name('Rebirth of a Fashionista: This Life Is Soo Last Season') == 'Rebirth-of-a-Fashionista-This-Life-Is-Soo-Last-Season'