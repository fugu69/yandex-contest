"""
Лекция 1 "Сложность, тестирование, особые случаи"

# Здача 1
Дана строка UTF-8. Найти самый частый в ней символ. Вывести любой, если символы повторяются.
"""

test_string = "Lovely Day"

def frequent_char(string):
    upper_string = string.upper()
    char_dict = {}
    for char in upper_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    max_value = 0
    freq_char = ""
    for key, value in char_dict.items():
        if value > max_value:
            max_value = value
            freq_char = key
    return f"The most frequent char in the stings is {freq_char}"

print(frequent_char(test_string))
    