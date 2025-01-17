from random import randint

nums = []
for _ in range(0, 20):
    nums.append(randint(1, 100))
print(nums)

for i in range(1, len(nums)):  # 1
    left_of = i + 1  # 2
    for j in range(i-1, -1, -1):  # 1
        if nums[i] > nums[j]:
            elm = nums.pop(i)
            nums.insert(left_of, elm)
        else:
            left_of = j
print(nums)
