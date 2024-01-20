from last_chars import last_chars

def test_last_chars_returns_last_8_characters():
    result = last_chars(8, 'All Code All Day')
    assert result == ' All Day'

def test_last_chars_returns_last_15_characters():
    result = last_chars(15, 'HTML, CSS, JavaScript, React')
    assert result == 'vaScript, React'

def test_last_chars_returns_last_character():
    result = last_chars(1, 'React')
    assert result == 't'

def test_last_chars_returns_last_3_characters():
    result = last_chars(3, 'Angular')
    assert result == 'lar'

def test_last_chars_returns_last_20_characters():
    result = last_chars(20, 'LearningFuze')
    assert result == 'LearningFuze'
