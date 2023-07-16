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
