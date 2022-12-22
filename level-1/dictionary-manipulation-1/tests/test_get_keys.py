from get_keys import getKeys

def testGetKeys():
  dave = {
      'firstName': 'David',
      'lastName': 'Thomas'
    }

  learningFuze = {
      'latitude': 33.6349,
      'attitude': 'sanguine',
      'longitude': 117.7405
    }

  empty = {}

  assert getKeys(dave) == ['firstName', 'lastName']
  assert getKeys(learningFuze) == ['latitude', 'attitude', 'longitude']
  assert getKeys(empty) == []
