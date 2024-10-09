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
    def __init__(self, value, left, right):
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
                print('node value', node.value)
                if node.value:
                    next_print.append(str(node.value))
                    if node.left:
                        new_nodes.append(node.left)
                    if node.right:
                        new_nodes.append(node.right)
                else:
                    next_print.append('N')
            
            stop = True
            for item in next_print:
                if item != 'N':
                    stop = False
            
            if stop:
                break
            else:
                print(' '.join(next_print))
                
            cur_nodes = new_nodes.copy()
                
    
# stack = Stack()
# stack.push('a')
# stack = stack.convert()
# stack.push('b')
# stack = stack.convert()
# stack.push('c')

# print(stack.items)


# queue = Queue()
# queue.push('a')
# queue.push('b')
# queue.push('c')
# queue.push('d')
# queue.push('e')
# queue.push('f')
# queue.push('g')
# queue = queue.convert()  # stack
# queue.pop()
# queue = queue.convert()  # queue
# queue.pop()
# queue.pop()
# queue = queue.convert()  # stack
# queue.pop()

# print(queue.items)

tree = Tree(Node(7, Node(3, None, None), Node(8, None, None)))
tree.add(Node(5, None, None))
tree.view()
