def reverseWord(str):
  reversed = ''
  i = len(str) - 1
  while i >= 0:
    reversed += str[i]
    i -= 1
  return reversed
