"""
6kyu: Roman Numerals Decoder
https://www.codewars.com/kata/roman-numerals-decoder/train/python

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21

"""
def solution(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
  int_val = 0
  for i in range(len(roman)):
      if i > 0 and rom_val[roman[i]] > rom_val[roman[i - 1]]:
          int_val += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
      else:
          int_val += rom_val[roman[i]]
  return int_val
