from is_vowel import isVowel

def test_is_vowel():
  assert isVowel('L') == False
  assert isVowel('f') == False
  assert isVowel('Z') == False
  assert isVowel('a') == True
  assert isVowel('E') == True
  assert isVowel('I') == True
  assert isVowel('o') == True
  assert isVowel('u') == True
