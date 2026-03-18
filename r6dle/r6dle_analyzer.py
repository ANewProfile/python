from pprint import pprint

from r6_data import ATTACKERS, DEFENDERS, OPERATORS
from r6dle import op_to_output

def average_operators_remaining():
    possible_remaining = {}

    for operator in OPERATORS.keys():
        possible_remaining[operator] = []
        for i, target1 in enumerate(OPERATORS.keys()):
            output = op_to_output(operator, target1)
            possible_remaining[operator].append(0)
            for target2 in OPERATORS.keys():
                if op_to_output(operator, target2) == output:
                    possible_remaining[operator][i] += 1

    averages = {}

    for operator in OPERATORS.keys():
        average = sum(possible_remaining[operator]) / len(possible_remaining[operator])
        averages[operator] = average

    best_op = None
    best_op_average_remaining = 10000000
    for operator in OPERATORS.keys():
        if averages[operator] < best_op_average_remaining:
            best_op_average_remaining = averages[operator]
            best_op = operator

    print(best_op, best_op_average_remaining)

def get_operators_remaining(guess):
    output1 = int(input("What is the correctness of the operators gender? "))
    output2 = int(input("What is the correctness of the operators role? "))
    output3 = int(input("What is the correctness of the operators side? "))
    output4 = int(input("What is the correctness of the operators speed? "))
    output5 = int(input("What is the correctness of the operators country? "))
    output6 = int(input("What is the correctness of the operators org? "))
    output7 = int(input("What is the correctness of the operators squad? "))
    output8 = int(input("What is the correctness of the operators year? "))
    output = [output1, output2, output3, output4, output5, output6, output7, output8]

    possible_operators = []
    for operator in OPERATORS.keys():
        if op_to_output(guess, operator) == output:
            possible_operators.append(operator)
    
    print(possible_operators)

get_operators_remaining(input("Which operator did you guess? "))

