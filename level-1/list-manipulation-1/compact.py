def compact(array):
  arr = []
  i = 0
  while i < len(array):
    if array[i]:
      arr.append(array[i])
    i += 1
  return arr
