import sys

def find_node_coords(node_triplet, nodes) -> tuple:
    node_triplet += ' = ('
    node_index = nodes.find(node_triplet)
    return (''.join([nodes[node_index+7], nodes[node_index+8], nodes[node_index+9]]), ''.join([nodes[node_index+12], nodes[node_index+13], nodes[node_index+14]]))
# print(find_node_coords('BBB', 'AAA = (BBB, CCC)\nBBB = (CCC, DDD)'))

def intify_pattern(pattern):
    intified_pattern = ''
    for char in pattern:
        if char.lower() == 'r':
            intified_pattern += '1'
        else:
            intified_pattern += '0'

    return intified_pattern

def main(node_set, pattern) -> int:
    turns = 0
    pointer_node = None
    pattern_index = 0
    pointer_pattern = pattern[pattern_index]
    pointer_node = find_node_coords('AAA', node_set)
    int_pattern = intify_pattern(pattern)
    while pointer_node != 'ZZZ':
        if pointer_node != 'ZZZ':
            pattern_index += 1
            try:
                pointer_pattern = int(int_pattern[pattern_index])
                pointer_node = find_node_coords(pointer_node[pointer_pattern], node_set)
                turns += 1
            except IndexError:
                pattern_index = 0
                pointer_pattern = int(int_pattern[pattern_index])
                pointer_node = find_node_coords(pointer_node[pointer_pattern], node_set)
                turns += 1

    return turns

if __name__ == '__main__':
    nodes = open('Day_8_Input.txt', 'r').read()
    pattern = sys.argv[-1]
    print(f'It takes {main(nodes, pattern)} turns to get to ZZZ from AAA')
