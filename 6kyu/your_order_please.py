"""
6kyu: Your order,please
https://www.codewars.com/kata/your-order-please/train/python

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
"""
def order(sentence):
  rslt = []
  sentence = sentence.split(" ")
  for i in range(1, len(sentence)+1):
      for a in range(0, len(sentence)):
          if str(i) in sentence[a]:
              rslt.append(sentence[a])
  return " ".join(rslt)