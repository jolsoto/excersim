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
