from initial import initial

def test_initial():
  assert initial(['foo', 'bar', 'baz']) == ["foo", "bar"]
  assert initial([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5]
  assert initial([True, False, False, True]) == [True, False, False]
  assert initial([]) == []
