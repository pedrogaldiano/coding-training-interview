def rotLeft(a, d):
    length = len(a)

    if d > length:
        d = d % length

    if d == length or d == 0:
        return a

    for i in range(d):
        temp = a[0]
        a.pop(0)
        a.append(temp)
    return a



x = [1,2,3,4,5]
print(rotLeft(x, 15))