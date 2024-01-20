from truncate import truncate

def test_truncate_truncates_all_code_all_day_to_8_characters():
    result = truncate(8, 'All Code All Day')
    assert result == 'All Code...'

def test_truncate_truncates_html_css_js_react_to_15_characters():
    result = truncate(15, 'HTML, CSS, JavaScript, React')
    assert result == 'HTML, CSS, Java...'

def test_truncate_truncates_react_to_1_character():
    result = truncate(1, 'React')
    assert result == 'R...'

def test_truncate_truncates_empty_string_to_5_characters():
    result = truncate(5, '')
    assert result == '...'

def test_truncate_truncates_learningfuze_to_20_characters():
    result = truncate(20, 'LearningFuze')
    assert result == 'LearningFuze...'
