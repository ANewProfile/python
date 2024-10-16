# normal binary search tree, BUT each node contains a counter for the # of times that value is added, and duplicates do not exist

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.counter = 1

class CounterTree:
    def __init__(self, root: Node):
        self.root = root
    
    def add(self, node: Node):
        last_node = None
        current_node = self.root  # Node(a, None, None, 1)
        go = False
        go_left = False
        while current_node:
            print(current_node.value, node.value)
            if current_node.value == node.value:
                current_node.counter += 1
                break
            go = True
            
            # if current_node.left:
            #     last_node = current_node
            #     current_node = current_node.left
            #     continue
            # if current_node.right:
            #     last_node = current_node
            #     current_node = current_node.right
            #     continue
                
            if current_node.value > node.value:
                print('left')
                last_node = current_node
                go_left = True
                current_node = current_node.left
            else:
                print('right')
                last_node = current_node
                go_left = False
                print(current_node.value, current_node.left, current_node.right, current_node.counter)
                current_node = current_node.right
                print(current_node)
        if go:
            if go_left:
                last_node.left = node
            else:
                last_node.right = node
    
    def get_nodes_counters(self):
        nodes = []
        current_node = self.root
        while current_node:
            if current_node.left:
                nodes.append(current_node.counter)
                current_node = current_node.left
            elif current_node.right:
                nodes.append(current_node.counter)
                current_node = current_node.right
            else:
                break
        
        print(nodes)
        return nodes

def make_tree(letters):
    tree = CounterTree(Node(letters[0], None, None))  # Tree(root= Node(a, None, None, 1))
    for i in range(1, len(letters)):
        # print(f"{letters} at {i} is {letters[i]}")
        tree.add(Node(letters[i], None, None))
    
    return tree

def output_from_tree(tree):
    return sum(tree.get_nodes_counters())

def main(input):
    letters = [char for char in input]  # [a, b, r, a, c, a, d, a, b, r, a, c, a, b, o, b]
    tree = make_tree(letters)  # 
    
    return output_from_tree(tree)

print(main('abracadabracabob'))
