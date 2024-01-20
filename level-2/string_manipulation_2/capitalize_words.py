def capitalize_words(string):
  lowercase = string.lower()
  string_arr = lowercase.split(' ')
  wrd = ''
  str = ''
  for i in range(len(string_arr)):
      letter = list(string_arr[i])
      upper_case = letter[0].upper()

      if i == len(string_arr) - 1:
          wrd += upper_case + string_arr[i][1:]
      else:
          wrd += upper_case + string_arr[i][1:] + ' '

  return wrd
