from random import randint
from time import time

nums = []
for _ in range(0, 25):
    nums.append(randint(1, 30))

def sort(nums, index=0, swapped=False):
    if index == len(nums) - 1:
        if not swapped:
            return nums
        else:
            return sort(nums[:-1], swapped=False) + [nums[-1]]

    new_swapped = swapped
    new_nums = nums.copy()
    if nums[index] > nums[index + 1]:
        new_nums[index], new_nums[index + 1] = new_nums[index + 1], new_nums[index]
        new_swapped = True
    
    return sort(new_nums, index + 1, new_swapped)

print(nums)

start = time()
nums = sort(nums)
print(f'Took: {time() - start}')

print(nums)
