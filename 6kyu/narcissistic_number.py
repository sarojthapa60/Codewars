"""
6kyu: Does my number look big in this?
https://www.codewars.com/kata/does-my-number-look-big-in-this/train/python

A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
"""
def narcissistic( value ):
    power = len(str(value))
    return sum(int(i) ** power for i in str(value)) == value
