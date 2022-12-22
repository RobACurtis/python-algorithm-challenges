def isVowel(string):
  vowels = {
    'a':'a',
    'e':'e',
    'i' :'i',
    'o':'o',
    'u':'u'
    }
  i = 0
  while i < len(string):
    letter = string[i].lower()
    if letter in vowels:
     return True
    else:
       return False
