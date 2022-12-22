def reverse(array):
  reverse = []
  i = len(array) - 1
  while i >= 0:
    reverse.append(array[i])
    i -= 1
  return reverse
