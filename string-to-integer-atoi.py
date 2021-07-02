def mine():
    s = "00000-42a1234"
    s = s.strip()
    signal = ['+', '-']

    if s == '':
        return 0
    elif len(s) == 1 and s in signal:
        return 0
    elif not(s[0].isdigit() or s[0] in signal):
        return 0
    elif s[0] in signal and s[1] in signal:
        return 0

    neg = 1
    nums = ''
    for i in s:
        if i == '+':
            pass
        elif i == '-':
            neg = -1
        elif i.isdigit():
            nums += i
        else:
            break
    
    
    while nums[0] == '0':
        nums = nums[1:]

    nums = int(nums) * neg

    if nums > (2 ** 31) -1:
        return (2 ** 31) -1

    elif nums < (-2 ** 31):
        return (-2 ** 31)    
    
    return nums

print(mine())