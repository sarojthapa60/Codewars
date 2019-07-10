"""
7kyu: Find the capitals
https://www.codewars.com/kata/find-the-capitals/train/python

Write a method that takes an array of hashes with two keys each: country or state, and capital. Keys may be symbols or strings

The method should return an array of sentences declaring the state or country and its capital.

Examples

state_capitals = [{state: 'Maine', capital: 'Augusta'}]
capital(state_capitals)[0] # returns "The capital of Maine is Augusta"

country_capitals = [{'country' => 'Spain', 'capital' => 'Madrid'}]
capital(country_capitals)[0] # returns "The capital of Spain is Madrid"

mixed_capitals: [{"state" => 'Maine', capital: 'Augusta'}, {country: 'Spain', "capital" => "Madrid"}]
capital(mixed_capitals)[0] # returns "The capital of Maine is Augusta"
"""
def capitals(word):
    return [i for i, a in enumerate(word) if a.isupper()] 