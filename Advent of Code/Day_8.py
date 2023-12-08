def find_node_coords(node_triplet, nodes):
    node_triplet += ' = ('
    node_index = nodes.find(node_triplet)
    return (''.join([nodes[node_index+7], nodes[node_index+8], nodes[node_index+9]]), ''.join([nodes[node_index+12], nodes[node_index+13], nodes[node_index+14]]))

print(find_node_coords('BBB', 'AAA = (BBB, CCC)\nBBB = (CCC, DDD)'))
