"""
6kyu: Who likes it?
https://www.codewars.com/kata/who-likes-it/train/python

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.
"""
def likes(names):
    textToReturn = ""
    
    if (len(names)) == 0:
        textToReturn = "no one likes this"
    elif (len(names)) == 1:
        textToReturn = str(names[0]) + " likes this"
    elif (len(names)) > 1 and len(names) < 4:
        for name in range(0, len(names) - 1):
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]    
        textToReturn = textToReturn + " and " + str(names[len(names) - 1]) + " like this"     
    else:
        for name in range(0, 2):
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]
        textToReturn = textToReturn + " and " + str(len(names) - 2) + " others like this"
        
    return textToReturn    
        