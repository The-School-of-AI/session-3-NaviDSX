def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
    '''

    if base < 2 or base >= 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    if len(digit_map)<base:
        raise ValueError('digit_map length is lesser than the base')
    for l in digit_map:
        if digit_map.count(l) > 1:
            raise ValueError('Characters repeating in digit_map')
    if base < len(digit_map):
        raise ValueError("Digit_map is not long enough to encode the digit")
    if number == 0:
        return '0'

    sign = -1 if number < 0 else 1
    number *= sign

    digits = []
    while number > 0:
        number, m = divmod(number, base)
        digits.insert(0, m)



    encoding = ''.join([digit_map[d] for d in digits])

    if sign == -1:
        encoding = '-' + encoding
    return encoding


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    return eval(str(f_num).split('.')[0])

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    i=eval(str(f_num).split('.')[0])
    if len(str(f_num).split('.'))==1: d=0
    else: d=eval('0.' + str(f_num).split('.')[1])
    if i%2==0:
        if d>.5: i+=1
    elif d>=.5: i+=1
    return i

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    if len(str(f_num).split('.'))==1: d=0
    else: d=eval('0.' + str(f_num).split('.')[1])

    from fractions import Fraction
    f_num=Fraction(f_num).limit_denominator(1).numerator
    if f_num > 0 and d==.5: f_num+=1
    return f_num

