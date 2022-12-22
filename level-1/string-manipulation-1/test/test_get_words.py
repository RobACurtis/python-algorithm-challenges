from get_words import getWords

def test_get_words():
  assert getWords('LearningFuze') == ["LearningFuze"]
  assert getWords('Web Development') == ["Web", "Development"]
  assert getWords('Cascading Style Sheets') == ["Cascading", "Style", "Sheets"]
  assert getWords('European Computer Manufacturers Association') == ["European", "Computer", "Manufacturers", "Association"]
  assert getWords('') == []
