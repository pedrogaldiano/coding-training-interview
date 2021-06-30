x = -123456


neg = 1
if x < 0:
    neg = -1
    x = neg * x

x = str(x)
k = int(''.join((x[i] for i in range(len(x)-1, -1, -1))))

if k <= (2 ** 31) -1:
    # return k * neg
    print(k * neg)

# return 0
