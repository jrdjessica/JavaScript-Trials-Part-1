"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    print(even_nums)
    return even_nums


def get_odd_indices(items):
    results = []
    for i in range(len(items)):
        if i % 2 != 0:
            results.append(items[i])
    print(results)
    return results


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):
    num_list = []
    for nums in range(start, stop):
        num_list.append(nums)

    return num_list


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)


def snake_to_camel(string):
    camel_case = []
    word_list = string.split('_')
    for word in word_list:
        word = word[0].upper() + word[1:]
        camel_case.append(word)
    return ''.join(camel_case)


# print(snake_to_camel('hello_world'))


def longest_word_length(words):
    longest_word = ""
    for word in word:
        if len(word) > longest_word:
            longest_word = word

    return len(longest_word)


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return ''.join(result)


# print(truncate('hi***!!!! wooow'))


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

            if parens < 0:
                return False

    return parens == 0


def compress(string):
    compressed = []
    current_char = ""
    char_count = 0
    for char in string:
        if char != current_char:
            compressed.append(current_char)
            if char_count > 1:
                compressed.append(str(char_count))
            current_char = char
            char_count = 0
        char_count += 1

    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)


# print(compress('aabbaabb'))
