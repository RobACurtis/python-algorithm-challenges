from reverse import reverse

def test_reverse():
  assert reverse(['foo', 'bar', 'baz']) == ["baz", "bar", "foo"]
  assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
  assert reverse([False, True, False, True]) == [True, False, True, False]
  assert reverse([]) == []
