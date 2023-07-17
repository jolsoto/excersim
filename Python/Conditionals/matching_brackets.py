'''
Instructions
Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly. The string may also contain other characters, which for the purposes of this exercise should be ignored.
'''
def is_paired(input_string):
    stack = []
    opening = ["[", "{", "("]
    closing = ["]", "}", ")"]
    
    for char in input_string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if opening.index(last_open) != closing.index(char):
                return False
    
    return len(stack) == 0
