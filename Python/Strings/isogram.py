'''
Instructions
Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.
'''

def is_isogram(string):
    isogram=string.lower()
    isogram=isogram.replace('-',' ')
    isogram=isogram.replace(' ','')
    if not string or string.isspace(): 
        result= True
    for letter in isogram:
        if isogram.count(letter)>1:
            result= False
            break
        result= True
    return result
