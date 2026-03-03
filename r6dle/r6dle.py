from r6_data import OPERATORS


def op_to_output(guess, target):
    if guess == target:
        return [2, 2, 2, 2, 2, 2, 2, 2]

    guess_op = OPERATORS[guess]
    target_op = OPERATORS[target]

    output = []

    # Gender
    if guess_op["gender"] == target_op["gender"]:
        output.append(2)
    else:
        output.append(0)

    # Role
    roles_correct = 0
    for role in guess_op["role"]:
        if role in target_op["role"]:
            roles_correct += 1

    if roles_correct == 0:
        output.append(0)
    elif len(target_op["role"]) == 2:
        output.append(roles_correct)
    elif len(target_op["role"]) == 1:
        if len(guess_op["role"]) == 1:  # roles_correct can only be 1 if this if statement is executed
            output.append(2)
        else:
            output.append(1)
    else:
        raise Exception("You should never see this")
    
    # Side
    if guess_op["side"] == target_op["side"]:
        output.append(2)
    else:
        output.append(0)
    
    # Speed
    if guess_op["speed"] == target_op["speed"]:
        output.append(2)
    else:
        output.append(0)
    
    # Country
    if guess_op["country"] == target_op["country"]:
        output.append(2)
    elif guess_op["continent"] == target_op["continent"]:
        output.append(1)
    else:
        output.append(0)
    
    # Org
    if guess_op["org"] == target_op["org"]:
        output.append(2)
    else:
        output.append(0)
    
    # Squad
    if guess_op["squad"] == target_op["squad"]:
        output.append(2)
    else:
        output.append(0)
    
    # Year
    if int(guess_op["year"]) < int(target_op["year"]):
        output.append(2)
    elif int(guess_op["year"]) == int(target_op["year"]):
        output.append(1)
    else:
        output.append(0)
    
    return output
