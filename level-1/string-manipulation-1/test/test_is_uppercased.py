from is_upper_cased import isUpperCased

def test_is_uppercased():
  assert isUpperCased('LearningFuze') == False
  assert isUpperCased('HTML') == True
  assert isUpperCased('JavaScript') == False
  assert isUpperCased('CSS') == True
  assert isUpperCased('PHP') == True
