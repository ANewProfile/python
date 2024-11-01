class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: Node):
        self.structure = {1: [root]}
    
    def add(self, node: Node):
        if len(self.structure) == 0:
            self.structure[1] = [node]
        else:
            if len(self.structure[current_depth]) == 2 ** (current_depth - 1):
                parent_node = self.structure[current_depth][0]
                current_depth += 1
                
                parent_node.left = node
                current_node = parent_node.left
                
                self.structure[current_depth] = current_node
            else:
                depth_length = len(self.structure[current_depth])
                left_or_right = depth_length % 2  # 0=left, 1=right
                parent_index = depth_length // 2
                parent_depth = current_depth - 1
                parent_node = self.structure[parent_depth][parent_index]
                if left_or_right == 0:
                    parent_node.left = node
                    current_node = parent_node.left
                    self.structure[current_depth].append(current_node)
                else:
                    parent_node.right = node
                    current_node = parent_node.right
                    self.structure[current_depth].append(current_node)
        
        while current_node.value < parent_node.value:
            current_node.value, parent_node.value = parent_node.value, current_node.value
            current_node = parent_node
            current_depth -= 1
            
            if current_depth >= 2:
                current_pos = self.structure[current_depth].index(current_node)
                parent_node = self.structure[current_depth - 1][current_pos // 2]
    
    def view(self):
        for i in self.structure:
            for j in self.structure[i]:
                print(j.value, end=' ')
            print()

tree = Tree(Node('P'))
tree.add(Node('R'))
tree.add(Node('O'))
tree.add(Node('G'))
tree.add(Node('R'))
tree.add(Node('A'))
tree.add(Node('M'))
tree.add(Node('M'))
tree.add(Node('I'))
tree.add(Node('N'))
tree.add(Node('G'))