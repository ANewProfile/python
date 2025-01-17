from random import randint

nums = []
for _ in range(0, 20):
    nums.append(randint(1, 100))
print(nums)

for i in range(0, len(nums)):
    smallest = i
    for j in range(i, len(nums)):
        if nums[j] < nums[smallest]:
            smallest = j
            print(nums[smallest], smallest)
    print('next')

    nums[smallest], nums[i] = nums[i], nums[smallest]

print(nums)
