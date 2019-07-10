"""
8kyu: Sum of positive
https://www.codewars.com/kata/sum-of-positive/train/python

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""
def positive_sum(arr):
    list = []
    if len(arr) == 0:
        return 0
    for items in arr:
        if items > 0:
            list.append(items)
            
    return sum(list)    