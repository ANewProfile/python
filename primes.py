max_num = float(input('What number would you like to check primes(e.g. 100 will check for all prime numbers under 100)? '))
max_num = int(round(max_num, 0))
nums = []

for i in range(1, max_num):
    nums.append(True)

nums[0] = nums[1] = False

def filter_primes(nums):
    max_int = int(max(nums))
    number_set = [True] * max_int
    number_set[0] = number_set[1] = False
    en_num_set = enumerate(number_set)

    for num, isprime in en_num_set:
        if isprime is True and num <= max_int**1/2:
            for multiple in range(num**2, max_int, num):
                number_set[multiple] = False
    
    new_nums = [str(num) for num, tag in enumerate(number_set) if tag is True]

    return new_nums

nums = filter_primes([num for num in range(1, max_num)])
num_list = '\n'.join(nums)
print(f'Your list of primes is: \n{num_list}')
