from set_value import setValue

def testSetValue():
  dave = {
      'firstName': 'David',
    }

  learningFuze = {
      'latitude': 33.6349,
      'attitude': 'sanguine'
    }

  name = {}

  one = setValue(dave, 'lastName', 'Thomas')
  two = setValue(learningFuze, 'longitude', 117.7405)
  three = setValue(name, 'language', 'python')

  assert one['lastName'] == 'Thomas'
  assert two['longitude']== 117.7405
  assert three['language'] == 'python'
