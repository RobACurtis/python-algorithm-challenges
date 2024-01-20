def last_chars(length, input_string):
    str_list = list(input_string)
    reversed_str = str_list[::-1]
    del_str = reversed_str[:length]
    final_string = ''.join(reversed(del_str))
    return final_string
import pytest
