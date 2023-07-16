def is_armstrong_number(number):
    sum1=0
    for digit in str(number):
        sum1+=int(digit)**len(str(number))
    return sum1==number
