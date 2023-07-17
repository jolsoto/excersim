'''
Instructions
Implement a program that translates from English to Pig Latin.

Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below), but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").
Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
There are a few more rules for edge cases, and there are regional variants too. Check the tests for all the details.

Read more about Pig Latin on Wikipedia.
'''

def translate(text):
    vowels={'a','e','i','o','u'}
    con_sounds={'qu','st','ch','th','thr','rh'}
    vowel_sounds={'squ','sch'}
    result=[]
    for word in text.split(' '):
        if word[0] in vowels or word[:2] in ['xr','yt']:
            result.append(word+'ay')
        elif word[0] not in vowels:
            if word[0:3] in vowel_sounds:
                result.append(word[3:]+word[0:3]+'ay')
            elif word[0:3] in con_sounds:
                result.append(word[3:]+word[0:3]+'ay')
            elif word[0:2] in con_sounds:
                result.append(word[2:]+word[0:2]+'ay')
            else:
                result.append(word[1:]+word[0]+'ay')
    return (' '.join(result[:]))
