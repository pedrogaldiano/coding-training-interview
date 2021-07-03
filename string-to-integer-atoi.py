# O meu ganhou tururu, por pouquinho, mas nessas condições ganhou
def mine():
    s = "-000456813+5asa"
    s = s.strip()

    if len(s) <= 1:
        if not (s.isdigit()):
            return 0
    else:
        if not ((s[0] in ['+', '-'] or s[0].isdigit())):
            return 0
        # elif s[0] in ['+', '-'] and s[1] in ['+', '-']:
        #     return 0

    neg = 1
    if s[0] == '-':
        neg = -1
        s = s[1:]
    elif s[0] == '+':
        neg = 1
        s = s[1:]

    nums = ''
    for i in range(len(s)):
        if s[i].isdigit():
            nums += s[i]
        else:
            break

    if nums == '':
        return 0

    while nums[0] == '0':
        nums = nums[1:]
        if nums == '':
            return 0

    nums = int(nums) * neg

    if nums > (2 ** 31) -1:
        return (2 ** 31) -1
    elif nums < (-2 ** 31):
        return (-2 ** 31)    
    
    return nums

def dozoto():
    s = "-000456813+5asa"

    started = False
    start = 0
    sign = 1
    i = 0
    numList = []
    
    while i < len(s) and not started:
        if s[i] != ' ':
            if s[i] == '-' and i+1 < len(s) and s[i+1].isnumeric():
                sign = -1
                started = True
                start = i + 1
            elif s[i] == '+' and i+1 < len(s) and s[i+1].isnumeric():
                started = True
                start = i + 1
            elif s[i].isnumeric():
                started = True
                start = i
            else:
                return 0
        i += 1
                
    if not started:
        return 0
    
    i = start

    while i < len(s) and s[i].isnumeric():
        numList.append(s[i])
        i += 1
        
    ans = int(''.join(numList)) * sign
    if ans > 2**31 - 1:
        return 2**31 -1
    elif ans < -2**31:
        return -2**31
    else:
        return ans

import timeit

print('mine: ', timeit.timeit(mine, number=10000000))
print('dozoto: ', timeit.timeit(dozoto, number=10000000))