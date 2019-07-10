"""
7kyu: Two to One
https://www.codewars.com/kata/two-to-one/train/python

Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
def longest(s1, s2):
    assert s1.isalpha()
    assert s2.isalpha()
    s = list(set(s1+s2))
    s1s2 = sorted(s)
    return ''.join(s1s2)