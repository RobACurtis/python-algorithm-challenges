from compact import compact

def test_compact():
  assert compact([True, True, False, True]) == [True, True, True]
  assert compact([{}, None, {}]) == []
  assert compact([1, 2, 3, 4, 6, 7]) == [1, 2, 3, 4, 6, 7]
  assert compact([-3, 8, 9, 10, 11, 0, 13]) == [-3, 8, 9, 10, 11, 13]
  assert compact([[], None, None]) == []
  assert compact(['', 'foo', 'bar', '', 'baz', 'qux']) == ['foo', 'bar', 'baz', 'qux']
  assert compact([1, 'a', {}, [], True]) == [1, 'a', True]
