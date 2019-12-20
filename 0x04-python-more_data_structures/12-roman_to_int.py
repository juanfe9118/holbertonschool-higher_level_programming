#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        dec = [1, 5, 10, 50, 100, 500, 1000]
        rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        res = 0
        i = 0
        stlen = len(roman_string)
        while i < stlen:
            if roman_string[i:i+2] == 'IV':
                res += 4
                i += 2
            elif roman_string[i:i+2] == 'IX':
                res += 9
                i += 2
            elif roman_string[i:i+2] == 'XL':
                res += 40
                i += 2
            elif roman_string[i:i+2] == 'XC':
                res += 90
                i += 2
            elif roman_string[i:i+2] == 'CD':
                res += 400
                i += 2
            elif roman_string[i:i+2] == 'CM':
                res += 900
                i += 2
            else:
                idx = rom.index(roman_string[i])
                res += dec[idx]
                i += 1
        return res
    else:
        return 0
