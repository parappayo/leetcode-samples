

roman_subs = [
    (1000, ['M']),
    (900, ['C', 'M']),
    (500, ['D']),
    (400, ['C', 'D']),
    (100, ['C']),
    (90, ['X', 'C']),
    (50, ['L']),
    (40, ['X', 'L']),
    (10, ['X']),
    (9, ['I', 'X']),
    (5, ['V']),
    (4, ['I', 'V']),
    (1, ['I'])
]


def addRomanNumeral(char_list, num):
    for value, chars in roman_subs:
        if num >= value:
            char_list.extend(chars)
            return num - value


def intToRoman(num):
    result = []
    while num > 0:
        num = addRomanNumeral(result, num)
    return ''.join(result)
