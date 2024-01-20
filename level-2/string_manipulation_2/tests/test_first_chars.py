from first_chars import first_chars

def test_first_chars_returns_first_8_characters():
    result = first_chars(8, 'All Code All Day')
    assert result == 'All Code'

def test_first_chars_returns_first_15_characters():
    result = first_chars(15, 'HTML, CSS, JavaScript, React')
    assert result == 'HTML, CSS, Java'

def test_first_chars_returns_first_character():
    result = first_chars(1, 'React')
    assert result == 'R'

def test_first_chars_returns_first_3_characters():
    result = first_chars(3, 'Angular')
    assert result == 'Ang'

def test_first_chars_returns_first_5_characters():
    result = first_chars(5, '')
    assert result == ''

def test_first_chars_returns_first_20_characters():
    result = first_chars(20, 'LearningFuze')
    assert result == 'LearningFuze'
