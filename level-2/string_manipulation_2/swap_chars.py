def swap_chars(first_index, second_index, input_string):
    final_str = ''
    str_list = list(input_string)

    first_char = str_list.pop(first_index)
    str_list.insert(first_index, '')

    second_char = str_list.pop(second_index)

    str_list.insert(second_index, first_char)
    str_list.insert(first_index, second_char)

    final_str = ''.join(str_list)

    return final_str
