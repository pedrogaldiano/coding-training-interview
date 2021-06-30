# This way is faster, but the lets code don't leet you use it :c
def using_set():
    nums = [-1,0,0,0,0,3]
    nums[:] = list(set(nums))
    return len(nums.sort())

def using_while():
    nums = [0,0,1,1,1,2,2,3,3,4]
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i+1]
        else:
            i +=1
    return len(nums)


import timeit

print('Set:  ', timeit.timeit(using_set, number= 100000000))
print('While:  ', timeit.timeit(using_while, number= 100000000))

