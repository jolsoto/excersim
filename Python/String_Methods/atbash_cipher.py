'''
Instructions
Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.

The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such that the resulting alphabet is backwards. The first letter is replaced with the last letter, the second with the second-last, and so on.

An Atbash cipher for the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: zyxwvutsrqponmlkjihgfedcba
It is a very weak cipher because it only has one possible key, and it is a simple mono-alphabetic substitution cipher. However, this may not have been an issue in the cipher's time.

Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, leaving numbers unchanged, and punctuation is excluded. This is to make it harder to guess things based on word boundaries. All text will be encoded as lowercase letters.

Examples
Encoding test gives gvhg
Encoding x123 yes gives c123b vh
Decoding gvhg gives test
Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog
'''
import string
def encode(plain_text):
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    result = []
    count=0
    text=plain_text.lower()
    for char in text:
        if char.isalpha():
            index=alphabet.find(char)
            encoded_char=reversed_alphabet[index]
            result.append(encoded_char)
            count+=1
        elif char.isdigit():
            result.append(char)
            count += 1
        if count == 5:
            result.append(" ")
            count = 0
    return (''.join(result[:])).rstrip()
    

def decode(plain_text):
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    
    result = []
    count=0
    text=plain_text.lower()
    for char in text:
        if char.isalpha():
            index=alphabet.find(char)
            encoded_char=reversed_alphabet[index]
            result.append(encoded_char)
            count+=1
        elif char.isdigit():
            result.append(char)
            count += 1
        if count == 5:
            result.append(" ")
            count = 0
    return (''.join(result[:])).rstrip().replace(' ','')
