class Node:
    def __init__(self, value, left=None, right=None, task=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        if root:
            self.structure = {1: [root]}
        else:
            self.structure = {}
    
    def add(self, node: Node):
        if len(self.structure) == 0:
            self.structure[1] = [node]
            return
        else:
            current_depth = len(self.structure)
            if len(self.structure[current_depth]) == 2 ** (current_depth - 1):
                parent_node = self.structure[current_depth][0]
                current_depth += 1
                
                parent_node.left = node
                current_node = parent_node.left
                
                self.structure[current_depth] = [current_node]
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
                
    def remove(self):
        if len(self.structure) == 1:
            self.structure = {}
            return
        else:
            current_depth = len(self.structure)
            self.structure[1][0].value = self.structure[current_depth][-1].value
            self.structure[current_depth] = self.structure[current_depth][:-1]
            if len(self.structure[current_depth]) == 0:
                del(self.structure[current_depth])
            current_node = self.structure[1][0]
        
        while True:
            children = []
            if current_node.left and current_node.left.value < current_node.value:
                children.append(current_node.left)
            if current_node.right and current_node.right.value < current_node.value:
                children.append(current_node.right)
            
            if len(children) == 2:
                smaller_child = children[0] if children[0].value <= children[1].value else children[1]
            elif len(children) == 1:
                smaller_child = children[0]
            else:
                break
            
            current_node.value, smaller_child.value = smaller_child.value, current_node.value
            current_node = smaller_child
    
    def view(self):
        for i in self.structure:
            for j in self.structure[i]:
                print(j.value, end=' ')
            print()


def main(k, after, ints):
    tree = Tree()
    for _ in range(0, after+1):
        tree.add(Node(ints[0]))
        ints = ints[1:]
    tree.view()
    print()
    
    for _ in range(1, k):
        tree.remove()
    tree.view()
    print()
    
    return tree.structure[1][0].value


ints = [1, 4, 56, 4, 2, 5, 7,  9, 345, 76, 45, 23, 5, 76]
k = 5
after = 10
print(main(k, after, ints))

# 1 2 4 4 5 7 9 56 76 345
