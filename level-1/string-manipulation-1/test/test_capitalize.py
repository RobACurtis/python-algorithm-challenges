from capitalize import capitalize

def test_capitalize():
  assert capitalize('a') ==  'A'
  assert capitalize('link') ==  'Link'
  assert capitalize('tO')  ==  'To'
  assert capitalize('ThE') == 'The'
  assert capitalize('pAsT') == 'Past'
