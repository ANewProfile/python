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
        add_to = None
        cur_node = self.root
        
        while True:
            # print(cur_node.value)
            
            if cur_node.value == node.value:
                cur_node.counter += 1
                # print(f'added to counter {cur_node.value} \n\n')
                break
            
            add_to = cur_node
            if cur_node.left:
                cur_node = cur_node.left
                # print('going left', cur_node.value)
                continue
            elif cur_node.right:
                cur_node = cur_node.right
                # print('going right', cur_node.value)
                continue
            
            if add_to.value < node.value:
                add_to.right = node
            elif add_to.value > node.value:
                add_to.left = node
            # print(f'added {node.value} \n\n')
            break
    
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
        
        # print(nodes)
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
print(main('American Computer Science League'))
print(main('Python and Java are programming languages'))
print(main('Python and Java and java and python'))
print(main('the quick brown fox jumped over the lazy river'))
