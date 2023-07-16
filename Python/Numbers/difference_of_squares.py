'''
Instructions
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.
The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.
Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

You are not expected to discover an efficient solution to this yourself from first principles; research is allowed, indeed, encouraged. Finding the best algorithm for the problem is a key skill in software engineering.

'''
def square_of_sum(number):
    counter=1
    result=0
    while counter<=number:
        result=result+counter
        counter+=1
    result=result**2
    return result
def sum_of_squares(number):
    counter=1
    result=0
    while counter<=number:
        result=result+(counter**2)
        counter+=1
    return result  
def difference_of_squares(number):
    result=square_of_sum(number)-sum_of_squares(number)
    return result
