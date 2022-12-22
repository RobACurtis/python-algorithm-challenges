from get_values import getValues

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

  name = {}

  assert getValues(dave) == ['David', 'Thomas']
  assert getValues(learningFuze)  == [33.6349, 'sanguine', 117.7405]
  assert getValues(name) == []
