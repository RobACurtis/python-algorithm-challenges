def tail(array):
  if len(array) > 1:
    arr = []
    i = 1
    while i < len(array):
      arr.append(array[i])
      i += 1
    return arr
  else:
    return array
