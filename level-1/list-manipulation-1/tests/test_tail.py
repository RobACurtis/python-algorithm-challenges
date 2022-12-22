
from tail import tail

def test_tail():
  assert tail(['foo', 'bar', 'baz'])      == ["bar", "baz"]
  assert tail([1, 2, 3, 4, 5, 6])         == [2, 3, 4, 5, 6]
  assert tail([True, False, False, True]) == [False, False, True]
  assert tail([]) == []
