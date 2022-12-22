from last import last

def test_last():
  assert last(['foo', 'bar', 'baz'])  == "baz"
  assert last([1, 2, 3, 4, 5]) == 5
  assert last([False, True, False, True]) == True
  assert last([]) == None
