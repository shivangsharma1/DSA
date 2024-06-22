#insertinon in BST is O(log n)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if not root: return None

    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root: return None

    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root: return None

    postorder(root.left)
    postorder(root.right)
    print(root.val)