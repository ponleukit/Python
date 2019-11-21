def prime_nb(Num):
    counted = 0
    for i in range(1, Num):
        if ( Num%i == 0):
            counted = counted + 1
    if ( counted == 1):
        return True
    else:
        return False
prime_nb(12)
