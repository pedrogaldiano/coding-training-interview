def log():
    n = 94143178827

    if n == 1:
        return True
    if n % 3 != 0:
        return False

    while True:
        n /= 3
        if n == 1:
            return True
        elif n < 1:
            return False
    
def zoto():
    n = 94143178827

    if n > 1:
        while n % 3 == 0:
            n //= 3
    return n == 1

import timeit

print('meu: ', timeit.timeit(log, number = 10000000))
print('zooto: ', timeit.timeit(zoto, number = 10000000))