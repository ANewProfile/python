class Stack:
    def __init__(self, items=[]):
        self.items = items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            self.items.pop(-1)
    
    def convert(self):
        return Queue(self.items)

class Queue:
    def __init__(self, items=[]):
        self.items = items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            self.items.pop(0)
    
    def convert(self):
        return Stack(self.items)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: Node):
        self.root = root
    
    def add(self, node: Node):
        last_node = None
        current_node = self.root
        while current_node:
            if current_node.value >= node.value:
                last_node = current_node
                go_left = True
                current_node = current_node.left
            else:
                last_node = current_node
                go_left = False
                current_node = current_node.right
        
        if go_left:
            last_node.left = node
        else:
            last_node.right = node
    
    def view(self):
        cur_nodes = [self.root]
        while True:
            next_print = []
            new_nodes = []
            for node in cur_nodes:
                if node:
                    next_print.append(str(node.value))
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                else:
                    next_print.append('-')
                    new_nodes.append(None)
                    new_nodes.append(None)
            
            stop = True
            for item in next_print:
                if item != '-':
                    stop = False
            
            if stop:
                break
            else:
                print(' '.join(next_print))
                
            cur_nodes = new_nodes.copy()
    
    def get_internal_path_length(self):
        depth_on = 0
        total = 0
        all_nodes = {0: [self.root], 1: []}
        while True:
            done = False
            for node in all_nodes[depth_on]:
                missing = True
                if not node:
                    continue
                
                if node.left or node.right:
                    missing = False

                all_nodes[depth_on+1].append(node.left)
                all_nodes[depth_on+1].append(node.right)
                # print(all_nodes)
            
            if missing:
                done = True
            
            if not done:
                depth_on += 1
                all_nodes[depth_on+1] = []
            else:
                for depth, nodes in all_nodes.items():
                    for node in nodes:
                        if node:
                            total += depth
                            print(f'total {total}')
                    
                break
    
        return total

tree = Tree(Node('P'))
tree.add(Node('R'))
tree.add(Node('O'))
tree.add(Node('G'))
tree.add(Node('R'))
tree.add(Node('A'))
tree.add(Node('M'))
tree.view()
print(tree.get_internal_path_length())
