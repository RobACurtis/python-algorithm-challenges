
from num_vowels import num_vowels


def test_num_vowels_returns_5_for_all_code_all_day():
    input_str = 'All Code All Day'
    output = num_vowels(input_str)
    assert output == 5

def test_num_vowels_returns_5_for_html_css_javascript_react():
    input_str = 'HTML, CSS, JavaScript, React'
    output = num_vowels(input_str)
    assert output == 5

def test_num_vowels_returns_2_for_react():
    input_str = 'React'
    output = num_vowels(input_str)
    assert output == 2

def test_num_vowels_returns_3_for_angular():
    input_str = 'Angular'
    output = num_vowels(input_str)
    assert output == 3

def test_num_vowels_returns_0_for_empty_string():
    input_str = ''
    output = num_vowels(input_str)
    assert output == 0

def test_num_vowels_returns_5_for_learning_fuze():
    input_str = 'LearningFuze'
    output = num_vowels(input_str)
    assert output == 5
