def first_chars(length, input_string):
    str_list = list(input_string)
    str_list = str_list[:length]
    final_string = ''.join(str_list)
    return final_string
