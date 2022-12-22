from get_value import getValue

def testGetValue():
  dave = {
      'firstName': 'David',
      'lastName': 'Thomas'
    }

  learningFuze = {
      'latitude': 33.6349,
      'attitude': 'sanguine',
      'longitude': 117.7405
    }

  name = {
    'name': 'Tim',
    'language': 'JavaScript'
  }

  assert getValue(dave, 'firstName') == 'David'
  assert getValue(learningFuze, 'latitude') == 33.6349
  assert getValue(name, 'name') == 'Tim'
