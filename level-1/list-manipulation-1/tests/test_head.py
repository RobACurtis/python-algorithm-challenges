from head import head

def test_head():
  assert head(['foo', 'bar', 'baz']) == "foo"
  assert head([1, 2, 3, 4, 5]) == 1
  assert head([False, True, False, True]) == False
  assert head([]) == None
