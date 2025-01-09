import time
import random

list_items = 1_000

numbers = []
for i in range(0, list_items):
    numbers.append(random.randint(0, 1_000_000))

numbers.sort()

target = int(input('Enter the number you would like to search for: '))

left_side = 0
right_side = list_items - 1
middle = (right_side + left_side) // 2

iterations = 0
while True:
    if numbers[middle] == target:
        print(f'{target} is at index: {middle}')
        break
    
    if target > numbers[middle]:
        left_side = middle
    else:
        right_side = middle
    
    middle = (right_side + left_side) // 2
    if right_side == left_side and numbers[right_side] != target:
        print(f'{target} is not in the list')
        break

    print(f'left: {left_side}, right: {right_side}, iterations: {iterations}')
    print(f'left: {numbers[left_side]}, right: {numbers[right_side]}, target: {target}')
    
    iterations += 1
    time.sleep(0.25)

print(numbers)