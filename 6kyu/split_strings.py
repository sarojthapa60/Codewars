"""
6kyu: Split Strings
https://www.codewars.com/kata/split-strings/train/python

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
from itertools import izip_longest
def solution(s):
    return [''.join(a) for a in izip_longest(s[::2], s[1::2], fillvalue='_')]
    
print(solution('abcdef')) 
