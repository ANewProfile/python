nums = []
totalforavg = 0
add = 0
gpa = 0.0


def find_grade(grade, type, add, gpa):
    if type.upper() == 'S':
        pass
    elif type.upper() == 'H':
        add = 0.5
    elif type.upper() == 'AP':
        add = 1.0
    else:
        print('Invalid')

    if grade == 'A+' or grade == 'A':
        gpa = 4.0
    elif grade == 'A-':
        gpa = 3.7
    elif grade == 'B+':
        gpa = 3.3
    elif grade == 'B':
        gpa = 3.0
    elif grade == 'B-':
        gpa = 2.7
    elif grade == 'C+':
        gpa = 2.3
    elif grade == 'C':
        gpa = 2.0
    elif grade == 'C-':
        gpa = 1.7
    elif grade == 'D+':
        gpa = 1.3
    elif grade == 'D':
        gpa = 1.0
    elif grade == 'E' or grade == 'F':
        gpa = 0.0
    else:
        print('Invalid.')
    return gpa + add


thisorthat = input(
    'Do you want to [a]verage 4-scale GPA or [c]alculate GPA from a letter grade? ')
if thisorthat.lower() == "a":
    grades = input(
        'Enter your GPAs(4.0, 3.7, 2.3)(seperated by comma and space): ')
    grades = grades.split(",")
    for num in grades:
        num = num.strip()
        if num == ' ':
            pass
        else:
            nums.append(float(num))
    for num in nums:
        totalforavg += num
    totalnums = len(nums)
    print(f"Your GPA is: {totalforavg/totalnums}")

elif thisorthat.lower() == "c":
    lettergrade = input("What is your letter grade(A+, A, ..., D+, D, E, F)? ")
    type = input('Are you in a [s]tandard, [h]onors, or [AP] class? ')
    grade = find_grade(lettergrade, type, add, gpa)
    print(f'Your GPA for that class is {grade}')
else:
    print('Invalid.')
