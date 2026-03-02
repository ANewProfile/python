from r6_ops_data import OPERATORS


def op_to_output(guess, target):
    if guess == target:
        return [2, 2, 2, 2, 2, 2, 2, 2]

    guess_op = OPERATORS[guess]
    target_op = OPERATORS[target]

    output = []
    if guess_op["gender"] == target_op["gender"]:
        output.append(2)
    else:
        output.append(1)

    roles_correct = 0
    for role in guess_op["role"]:
        if role in target_op["role"]:
            roles_correct += 1

    if roles_correct == 0:
        output.append(0)

    if len(target_op["role"]) == 2:
        output.append(roles_correct)
    elif len(target_op["role"]) == 1:
        if (roles_correct == 1) and (len(guess_op["role"]) == 1):
            output.append(2)
        else:
            output.append(1)
    else:
        raise Exception("You should never see this")
