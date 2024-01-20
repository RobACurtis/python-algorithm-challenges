from swap_chars import swap_chars

def test_swap_chars_swaps_l_and_o_in_lodash():
    result = swap_chars(0, 1, 'lodash')
    assert result == 'oldash'

def test_swap_chars_swaps_R_and_t_in_React():
    result = swap_chars(0, 4, 'React')
    assert result == 'teacR'

def test_swap_chars_swaps_t_and_last_e_in_complete():
    result = swap_chars(6, 7, 'complete')
    assert result == 'compleet'

def test_swap_chars_swaps_L_and_F_in_LearningFuze():
    result = swap_chars(0, 8, 'LearningFuze')
    assert result == 'FearningLuze'

def test_swap_chars_swaps_J_and_R_in_HTML_CSS_JavaScript_React():
    result = swap_chars(11, 23, 'HTML, CSS, JavaScript, React')
    assert result == 'HTML, CSS, RavaScript, Jeact'
