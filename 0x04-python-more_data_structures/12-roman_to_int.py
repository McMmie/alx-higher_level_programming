#!/usr/bin/python3
def roman_to_int(roman_string) -> int:
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        roman_numerals = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000
                }
        previous, result = 0, 0

        for character in reversed(roman_string):
            value = roman_numerals[character]
            if value >= previous:
                result += value
            else:
                result -= value
            previous = value
        return result
