def num_vowels(input_string):
    lower_case = input_string.lower()
    num = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in lower_case:
        if char in vowels:
            num += 1

    return num
