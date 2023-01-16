from capitalize_word import capitalize_word

def test_capitalize_word():
  assert capitalize_word('broKeN') == 'Broken'
  assert capitalize_word('sEarChiNg') == 'Searching'
  assert capitalize_word('quEstIon') == 'Question'
  assert capitalize_word('javaScript') == 'JavaScript'
  assert capitalize_word('Python') == 'Python'
