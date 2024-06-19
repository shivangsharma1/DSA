class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

levels = []

def dft(node, level):
    if len(levels) == level:
        levels.append([])
    levels[level].append(node.data)

    if node.left:
        dft(node.left, level+1)
    if node.right:
        dft(node.right, level+1)

def levelordertraversaldft(root):
    
    if root is None:
        return levels

    else:
        dft(root, 0)
    return levels



root = Node(3)
root.left = Node(9)
root.right = Node(10)
root.right.left = Node(15)
root.right.right = Node(7)

result = levelordertraversaldft(root)
print(result)
``