def is_prime(num):
    if num < 0:
        return False
    list = []
    factors = []
    real = []
    for index in range(num + 1):
        list.append(index)
    list.remove(0)
    for i in list:
        number = num/i
        factors.append(number)
    for i in factors:
        if i % 1 == 0:
            real.append(i)
    if len(real) == 2 :
        return True
    else:
        return False
#----------------------------------------------------------------------------------OR------------------------------------------------------------------------------
def is_prime(num):
    if num < 0:
        return False
    factors = []
    for index in range(num + 1):
        if index != 0:
            number = num/index
            if number % 1 == 0:
                factors.append(index)
    if len(factors) == 2:
        return True
    else:
        return False
