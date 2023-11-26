'''
Introduction
You are starting a secret coding club with some friends and friends-of-friends. Not everyone knows each other, so you and your friends have decided to create a secret handshake that you can use to recognize that someone is a member. You don't want anyone who isn't in the know to be able to crack the code.

You've designed the code so that one person says a number between 1 and 31, and the other person turns it into a series of actions.

Instructions
Your task is to convert a number between 1 and 31 to a sequence of actions in the secret handshake.

The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary. Start at the right-most digit and move left.

The actions for each number place are:

00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump
10000 = Reverse the order of the operations in the secret handshake.
Let's use the number 9 as an example:

9 in binary is 1001.
The digit that is farthest to the right is 1, so the first action is wink.
Going left, the next digit is 0, so there is no double-blink.
Going left again, the next digit is 0, so you leave your eyes open.
Going left again, the next digit is 1, so you jump.
That was the last digit, so the final code is:

wink, jump
Given the number 26, which is 11010 in binary, we get the following actions:

double blink
jump
reverse actions
The secret handshake for 26 is therefore:

jump, double blink
Note
If you aren't sure what binary is or how it works, check out this binary tutorial.

To keep things simple (and to let you focus on the important part of this exercise), your function will receive its inputs as binary strings:

>>> commands("00011")
["wink", "double blink"]
'''

command_list={0:'wink',1:'double blink',2:'close your eyes',3:'jump',4:'reverse'}
def commands(binary_str):
    str1=[]
    if binary_str=='00000':
        return str1
    else:  
        command_ord=binary_str[::-1]
        for i,command in enumerate(command_ord):
            if command=='1':
                str1.append(command_list[i])
        if str1[-1]=='reverse':
            str2=str1[:-1]
            return str2[::-1]
        else:
            return str1
