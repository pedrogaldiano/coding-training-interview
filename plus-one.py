def long():
    digits = [1,2,3,4,5,6,7,8,9]

    new = (digits[-1] + 1)
    if new < 10:
        digits[-1] = new
        # print(digits)
        return digits

    s = ''
    for i in digits:
        s += str(i)
    value = str(int(s) + 1)
    # x = [int(i) for i in value]
    # print(x)
    return [int(i) for i in value]
    
# This way is faster :O
def short():
    digits = [1,2,3,4,5,6,7,8,9]

    digits = int(''.join(str(i) for i in digits)) + 1
    return list(str(digits))

import timeit

print('Long: ', timeit.timeit(long, number=1000000))
print('Short: ', timeit.timeit(short, number=1000000))