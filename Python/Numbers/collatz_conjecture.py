def steps(number):
    counter=0
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number>1:
            if number%2==0:
                number=number/2
            elif number%2!=0:
                number=(number*3)+1
            counter=counter+1
    return counter
