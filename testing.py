def isBadVersion(a):
    if a >= 171:
        return True
    else:
        return False
n = 200
x = 1


l = 1
r = n

while r >= l:
    print(l, r)
    mid = (r - l) // 2 + l

    if isBadVersion(mid):
        r = mid -1
    else:
        l = mid + 1
print(l)