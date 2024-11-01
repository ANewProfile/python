def get_left(node, structure, current_layer):
    return structure[current_layer+1][structure[current_layer][(structure[current_layer].index(node)-1) * 2]] if len(structure[current_layer+1]) <= (structure[current_layer].index(node)-1) * 2 else None

def get_right(node, structure, current_layer):
    return structure[(structure[current_layer][(structure[current_layer].index(node)-1) * 2]) + 1]  if len(structure[current_layer+1]) <= ((structure[current_layer].index(node)-1) * 2) + 1 else None
    

def check_structure(structure):
    current_layer = 1
    num_layers = len(structure)
    while current_layer <= num_layers:
        for node in structure[current_layer]:
            if node.left:
                if node.value >= node.left.value:
                    return False
            if node.right:
                if node.value >= node.right.value:
                    return False
        
        current_layer += 1
            
    return True

def swap_values(first_node, second_node):
    temp_value = first_node.value
    first_node.value = second_node.value
    second_node.value = temp_value
    
    return first_node, second_node

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: Node):
        self.structure = {1: [root], 2: []}
        self.depth_on = 2
    
    def add(self, node: Node):
        depth_check = self.depth_on
        
        
        self.structure[self.depth_on].append(node)
        
        parent = self.structure[self.depth_on-1][self.structure[self.depth_on].index(node)//2]
        if get_left(parent, self.structure, self.depth_on-1) == node:
            parent.left = node
        if get_right(parent, self.structure, self.depth_on-1) == node:
            parent.right = node
            
        if (2 ** (self.depth_on-1)) == len(self.structure[self.depth_on]):
            self.depth_on += 1
            self.structure[self.depth_on] = []
        
        current_node = node
        while True:
            if check_structure(self.structure):
                print('added %s' % (node.value))
                break
            
            parent = self.structure[depth_check-1][self.structure[depth_check].index(current_node)//2]
            print('swapping %s with %s' % (current_node.value, parent.value))
            if current_node.value <= parent.value:
                parent, current_node = swap_values(parent, current_node)
                
                current_node = parent
                depth_check -= 1
        
    
    def remove(self):
        last_node = self.structure[self.depth_on][-1]
        current_node = self.structure[1][0]
        current_node.value = last_node.value
        
        parent = self.structure[self.depth_on-1][self.structure[self.depth_on].index(last_node)//2]
        if parent.left == last_node:
            parent.left = None
        if parent.right == last_node:
            parent.right = None
        
        self.structure[self.depth_on].remove(last_node)
        
    
        while True:
            if check_structure(self.structure):
                break
            
            if current_node.value >= current_node.right.value or current_node.value >= current_node.left.value:
                if current_node.right.value >= current_node.left.value:
                    current_node, current_node.left = swap_values(current_node, current_node.left)
                    
                    current_node = current_node.left
                else:
                    current_node, current_node.right = (current_node, current_node.right)
                    
                    current_node = current_node.right
    
    def view(self):
        for i in range(1, len(self.structure)+1):
            printing = []
            for item in self.structure[i]:
                printing.append(str(item.value))
            print(" ".join(printing))
        
tree = Tree(Node('P', None, None))
tree.add(Node('R', None, None))
tree.add(Node('O', None, None))
tree.add(Node('G', None, None))
tree.add(Node('R', None, None))
tree.add(Node('A', None, None))
tree.add(Node('M', None, None))
tree.add(Node('M', None, None))
tree.add(Node('I', None, None))
tree.add(Node('N', None, None))
tree.add(Node('G', None, None))
tree.view()
