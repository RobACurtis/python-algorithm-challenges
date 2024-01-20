from capitalize_words import capitalize_words

def test_capitalize_words():
    assert callable(capitalize_words)

def test_capitalize_words_needs_solution():
    input_str = 'needs solution'
    output_str = capitalize_words(input_str)
    assert output_str == 'Needs Solution'

def test_capitalize_words_add_string_manipulation_practice():
    input_str = 'Add string manipulation practice.'
    output_str = capitalize_words(input_str)
    assert output_str == 'Add String Manipulation Practice.'

def test_capitalize_words_all_code_all_day():
    input_str = 'aLl CoDe aLl DaY'
    output_str = capitalize_words(input_str)
    assert output_str == 'All Code All Day'

def test_capitalize_words_languages():
    input_str = 'HTML, CSS, JavaScript, PHP, SQL'
    output_str = capitalize_words(input_str)
    assert output_str == 'Html, Css, Javascript, Php, Sql'
