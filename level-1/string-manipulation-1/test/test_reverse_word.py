from reverse_word import reverseWord

def test_reverse_word():
  assert reverseWord('foo') == "oof"
  assert reverseWord('rab') == "bar"
  assert reverseWord('LearningFuze') == "ezuFgninraeL"
  assert reverseWord('tpircSavaJ') == "JavaScript"
  assert reverseWord('racecar') == "racecar"
