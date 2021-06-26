import random

nums1 = [random.choice(range(1,10000)) for i in range(50)] + [0] * 50

nums2 = [random.choice(range(1,10000)) for i in range(50)]

print(nums1)
print(len(nums1))
print()
print(nums2)
print(len(nums2))