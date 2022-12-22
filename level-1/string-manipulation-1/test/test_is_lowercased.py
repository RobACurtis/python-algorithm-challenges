from is_lower_cased import isLowerCased

def test_is_lowercased():
  assert isLowerCased('LearningFuze') == False
  assert isLowerCased('zip-ties') == True
  assert isLowerCased('JavaScript') == False
  assert isLowerCased('burgers') == True
  assert isLowerCased('HTML') == False
