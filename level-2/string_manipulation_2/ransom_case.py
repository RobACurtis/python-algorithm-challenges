def ransom_case(word):
    str_lower = word.lower()
    arr = list(str_lower)
    result = ''

    for i in range(len(arr)):
        if i % 2 != 0:
            result += arr[i].upper()
        else:
            result += arr[i]

    return result
