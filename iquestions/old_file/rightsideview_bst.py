class Node:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def printview(root, level, maxlevel):
    if root is None:
        return
    
    if maxlevel[0]<level:
        print(root.data)
        maxlevel[0] = level

    printview(root.right, level+1, maxlevel)
    printview(root.left, level+1, maxlevel)


def rightview(root):
    maxlevel = [0]
    printview(root, 1, maxlevel)



# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

rightview(root)