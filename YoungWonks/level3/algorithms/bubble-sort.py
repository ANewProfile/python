from random import randint
from time import time

nums = []
for _ in range(0, 1000):
    nums.append(randint(1, 30))

print(nums)
start = time()
for j in range(0, len(nums)):
    swapped = False
    for i in range(len(nums)-j):
        if i < len(nums)-1:
            if nums[i+1] < nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
    
    if not swapped:
        break

print(f'Took: {time() - start}')
print(nums)
