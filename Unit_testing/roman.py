# import unittest

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def to_roman(n):
    '''returns roman numeral from arabic numeral'''
    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be between 1 and 4000)')
    
    if not isinstance(n, int):
        raise NotIntegerError('Non-integers can not be converted')
        
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

class OutOfRangeError(ValueError):
    pass

class NotIntegerError(ValueError):
     pass


def from_roman(s):
    '''convert roman numerals to integers'''
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result 