# Python Language

# Import the necessary modules
import random

# Create a list of first names, last names, and a full name
first_names = ["Liam", "Grayson", "Jaina", "Cassandra",
               "Ozzy", "Teddy", "Skyler", "Theo", "Truman"]
last_names = ["O\'Riain", "Bardin", "Considine", "Olszewski",
              "Chen", "Palchik", "Ferguson", "Kokones", "Hibbard"]
count = 0
name = ""


def create_names(firstname, lastname, name, count):
    availableNums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    names = []
    while count < 100:
        num1 = random.choice(availableNums)
        num2 = random.choice(availableNums)
        name = firstname[num1] + " " + lastname[num2]
        count += 1
        names.append(name)
    return names


x = create_names(first_names, last_names, name, count)
print('\n'.join(x))
