# session-3-nmeva
session-3-nmeva created by GitHub Classroom

### 1. encoded_from_base10(number, base, digit_map)
- Description
	- Function takes all inputs in a base10 format - hence base10.
	- Function can be modifed to get Binary and Hexadecimal formats provided by bin() and hex() functions.
	- Takes the number, the base to which it has to be encoded into
		and the custom digit map and outputs the encoded number.
- Inputs
	- (number, base, digit_map)
	- Ex. 10,2,AB
- Outputs
	- Encoded Number
	- Ex. BABA
- Logic

``` python
#digits = [] Create a list container
#run loop until number is zero (4 times)
#divmod(number, base)-- For 10,2 One(10,2)->(5,0); Two-(5,2)->(2,1);Three(2,2)->(1,0);Four(1,2)->(1,1)
#digits.insert(0, m) -- Four(1)-> Three(0)-> Two(1)-> One(0) Insert in 0th index, First from left.

digits = []
while number > 0:  
	number, m = divmod(number, base)  
	digits.insert(0, m) 

#digits = [1,0,1,0]
#digit_map=[A,B]/'AB'
#digit_map[d] for d in digits] picks A or B corresponding to 0 or 1
#''.join - joins the single list output to a string ''

encoding = ''.join([digit_map[d] for d in digits])

```
- Notes
```
All ValueError error conditions are captured.

divmod() takes two parameters:
x - a non-complex number (numerator)
y - a non-complex number (denominator)

divmod() returns
(q, r) - a pair of numbers (a tuple) consisting of quotient q and remainder r

If x and y are integers, the return value from divmod() is same as (a // b, x % y).
If either x or y is a float, the result is (q, x%y). Here, q is the whole part of the quotient.
```


### 2.float_equality_testing(a, b)

- Inputs
	- a,b
	- rel_tol = 1e-12
    - abs_tol = 1e-05
- Outputs
	- abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
- [Notes](https://docs.python.org/3/library/math.html)

```markdown
** math.isclose
- Return True if the values a and b are close to each other and False otherwise.
- Whether or not two values are considered close is determined according to given absolute and relative tolerances.
- rel_tol is the relative tolerance – it is the maximum allowed difference between a and b, relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, pass rel_tol=0.05. The default tolerance is 1e-09, which assures that the two values are the same within about 9 decimal digits. rel_tol must be greater than zero.
- abs_tol is the minimum absolute tolerance – useful for comparisons near zero. abs_tol must be at least zero.
- If no errors occur, the result will be: **abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
```


### 3.manual_truncation_function(f_num)

- Description
	- Returns Truncated Integer
- Logic
``` python
#Used the string method, we can use the Fraction method too.
#str(f_num)-converts number to string
#.split('.')[0] - splits the string at the decimal point and take the first element
#tested for without decimal and also 0
#eval converts the string to int
eval(str(f_num).split('.')[0])
```
- [Notes](https://docs.python.org/3/library/math.html)
```markdown

** math.trunc(x)
Return the Real value x truncated to an Integral (usually an integer). Delegates to x.__trunc__().
```

### 4.manual_rounding_function(f_num)

- Description
	- ** Bankers rounding:
	  if two multiples are equally close, rounding is done toward the even choice
- Inputs
	- ndigits is ignored
- Outputs
	- Only Integer values are outputted
- Logic
``` python
# i is the integer part of the input, first element of computed list.
i=eval(str(f_num).split('.')[0])

# d is the decimal part which is zero for integers,
# otherwise the second element of computed list.
if len(str(f_num).split('.'))==1: d=0
else: d=eval('0.' + str(f_num).split('.')[1])

#Compute Bankers Rounding:
#If i is even, round up only if d is greater than .5
#Otherwise round up if d is equal or greater than .5

if i%2==0:
	if d>.5: i+=1
elif d>=.5: i+=1
return i
```

- [Notes](https://docs.python.org/3/library/functions.html#round)

```markdown
** round(number[, ndigits])
Return number rounded to ndigits precision after the decimal point.
If ndigits is omitted or is None, it returns the nearest integer to its input.

For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits;
** Bankers rounding:
if two multiples are equally close, rounding is done toward the even choice
for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2).
Any integer value is valid for ndigits (positive, zero, or negative).
The return value is an integer if ndigits is omitted or None.
Otherwise the return value has the same type as number.

```


### 5.rounding_away_from_zero(f_num)

- Description
	- Based on - midvalue is always rounded AWAY from ZERO.
		Ex: +0.5 --> +1
			+1.5 --> +2
			-0.5 --> -1
			-1.5 --> -2
- Inputs
	- ndigits is ignored
- Outputs
	- Only Integer values are outputted
- Logic
``` python
#numerator is always lowest hence will be away from zero for postive numbers
#for this reason, decimal value (d) is computed and incremented in such cases.
#limit_denominator is set to 1 to extract the numerator

#decimal value is computed to arrive at tie
if len(str(f_num).split('.'))==1: d=0
else: d=eval('0.' + str(f_num).split('.')[1])

#numerator is extracted by limiting denominator to 1
from fractions import Fraction
f_num=Fraction(f_num).limit_denominator(1).numerator

#since numerator is rounded to lowest in case of a positive tie
#tie is computed earlier and incremented in case of positive numbers

if f_num > 0 and d==.5: f_num+=1
```
- [Notes](https://docs.python.org/3/library/fractions.html#module-fractions)
```markdown
The fractions module provides support for rational number arithmetic.
A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.

** numerator
Numerator of the Fraction in lowest term.
** limit_denominator(max_denominator=1000000)
Finds and returns the closest Fraction to self that has denominator at most max_denominator.
```


