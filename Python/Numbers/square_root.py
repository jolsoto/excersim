'''
Instructions
Given a natural radicand, return its square root.

Note that the term "radicand" refers to the number for which the root is to be determined. That is, it is the number under the root symbol.

Check out the Wikipedia pages on square root and methods of computing square roots.

Recall also that natural numbers are positive real whole numbers (i.e. 1, 2, 3 and up).

How this Exercise is Structured in Python
Python offers a wealth of mathematical functions in the form of the math module and built-ins such as pow() and sum(). However, we'd like you to consider the challenge of solving this exercise without those built-ins or modules.

While there is a mathematical formula that will find the square root of any number, we have gone the route of only testing natural numbers (positive integers).
'''

def square_root(number):
    if number<0:
        raise ValueError("Only positive integers are allowed")
    elif number==0:
        result=0
    else:
        result=0
        minus=1
        while number>0:
            number=number-minus
            minus+=2
            result+=1
    return result
