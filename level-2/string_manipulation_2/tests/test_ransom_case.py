from ransom_case import ransom_case

def test_ransom_case_returns_foo_for_foo():
    input_str = 'foo'
    output = ransom_case(input_str)
    assert output == 'fOo'

def test_ransom_case_returns_quux_for_quux():
    input_str = 'QUUX'
    output = ransom_case(input_str)
    assert output == 'qUuX'

def test_ransom_case_returns_waldo_for_waldo():
    input_str = 'WaldO'
    output = ransom_case(input_str)
    assert output == 'wAlDo'

def test_ransom_case_returns_javascript_for_javascript():
    input_str = 'JavaScript'
    output = ransom_case(input_str)
    assert output == 'jAvAsCrIpT'

def test_ransom_case_returns_learningfuze_for_learningfuze():
    input_str = 'LearningFuze'
    output = ransom_case(input_str)
    assert output == 'lEaRnInGfUzE'
