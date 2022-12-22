from to_object import toObject

def testSetValue():
  assert toObject(['lastName', 'Thomas']) == {'lastName': 'Thomas'}
  assert toObject(['longitude', 117.7405]) == {'longitude': 117.7405}
  assert toObject(['language', 'python']) == {'language': 'python'}
