def truncate(length, input_string):
    arr = list(input_string)
    del arr[length:]

    result = ''
    for char in arr:
        result += char

    result += '...'
    return result
