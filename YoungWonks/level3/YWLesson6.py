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
        if ((len(self.structure[self.depth_on])-1) ** 2) == len(self.structure[self.depth_on]):
            self.depth_on += 1
        
        current_node = node
        while True:
            if check_structure(self.structure):
                break
            
            parent = self.structure[depth_check-1][self.structure[depth_check].index(current_node)//2]
            if current_node.value <= parent.value:
                temp_value = parent.value
                parent.value = current_node.value
                current_node.value = temp_value
                
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
                    temp_value = current_node.value
                    current_node.value = current_node.left.value
                    current_node.left.value = temp_value
                    
                    current_node = current_node.left
                else:
                    temp_value = current_node.value
                    current_node.value = current_node.right.value
                    current_node.right.value = temp_value
                    
                    current_node = current_node.right
    
    def view(self):
        for i in range(1, len(self.structure)+1):
            printing = []
            for item in self.structure[i]:
                printing.append(str(item.value))
            print(" ".join(printing))
        
tree = Tree(Node(7, None, None))
tree.add(Node(8, None, None))
tree.add(Node(12, None, None))
tree.view()
print('-------------')
tree.remove()
tree.view()
print('-------------')
tree.add(Node(3, None, None))
tree.view()
