import random

list_items = 1_000

numbers = []
for i in range(0, list_items):
    numbers.append(random.randint(0, 100))

numbers.sort()

target = int(input('Enter the number you would like to search for: '))

left_side = 0
right_side = list_items - 1
middle = (right_side + left_side) // 2
found_loc = None

while True:
    if numbers[middle] == target:
        found_loc = middle
        break
    
    if target > numbers[middle]:
        left_side = middle
    else:
        right_side = middle
    
    middle = (right_side + left_side) // 2
    if right_side == left_side and numbers[right_side] != target:
        break

    if (right_side - left_side) == 1 and numbers[right_side] != target:
        break

if found_loc:
    left_bound = found_loc
    right_bound = found_loc
    found_left = False
    found_right = False

    while not found_left:
        if numbers[left_bound] == target:
            if left_bound == 0:
                found_left = True
            else:
                left_bound -= 1
        else:
            left_bound += 1
            found_left = True
    
    while not found_right:
        if numbers[right_bound] == target:
            if right_bound == list_items - 1:
                found_right = True
            else:
                right_bound += 1
        else:
            right_bound -= 1
            found_right = True

if found_loc:
    print(numbers[left_bound:right_bound+1])
